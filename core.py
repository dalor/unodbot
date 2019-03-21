from flask import Flask, request
from dtelbot import Bot, inputmedia as inmed, reply_markup as repl, inlinequeryresult as iqr
from game_controller import GameController
import os
from pprint import pprint

app = Flask(__name__)

b = Bot(os.environ['BOT_ID'])
g = GameController()

my_cards_button =  [repl.inlinekeyboardbutton('Мои карты', switch_inline_query_current_chat='')]

def send_status(game, reply_to_message_id=None):
    if game.play:
        reply_markup = [
            [repl.inlinekeyboardbutton('Взять', callback_data='get')],
            my_cards_button
        ]
        game.message_id = b.msg(str(game), chat_id=game.id, parse_mode='HTML',
                reply_markup=repl.inlinekeyboardmarkup(reply_markup),
                reply_to_message_id=reply_to_message_id if reply_to_message_id else ''
                ).send()['result']['message_id']

def update_status(game):
    if game.play:
        reply_markup = [
            [repl.inlinekeyboardbutton('Взять', callback_data='get')] if not game.players.now.is_get_card else [repl.inlinekeyboardbutton('Следущий', callback_data='pass')],
            my_cards_button
        ]
        b.edittext(str(game), chat_id=game.id, message_id=game.message_id, reply_markup=repl.inlinekeyboardmarkup(reply_markup), parse_mode='HTML').send()

def clear_reply_markup(chat_id, message_id):
    b.editreplymarkup(chat_id=chat_id, message_id=message_id, reply_markup='').send()

def is_norm(a, player):
    if player and player == player.game.players.now:
        if a.data['message']['message_id'] != player.game.message_id:
            clear_reply_markup(a.data['message']['chat']['id'], a.data['message']['message_id'])
        else:
            return True
            
@b.message('/new0')
def new_game(a):
    if g.new_game(a.data['chat']['id']):
        a.msg('Игра была успешно создана\n/join0 что-бы зайти').send()
    else:
        a.msg('Игра уже была создана').send()

@b.message('/join0')
def join_game(a):
    game = g.get_game(a.data['chat']['id'])
    if not game:
        a.msg('Игры не существует\n/new0 что-бы создать').send()
    else:
        if g.new_player(game, a.data['from']['id'], a.data['from']['first_name'] + (' ' + a.data['from']['last_name'] if 'last_name' in a.data['from'] else '')):
            a.msg('Успешно зашел').send()
            update_status(game)
        else:
            a.msg('Что-то пошло не так').send()
        
@b.message('/leave0')
def leave_game(a):
    player = g.del_player(a.data['from']['id'])
    if player:
        a.msg('Ok').send()
        update_status(game)
    else:
        a.msg('Ты не выйдешь!')

@b.message('/start0')
def start_game(a):
    player = g.get_player(a.data['from']['id'], True)
    if player and not player.game.play:
        player.game.start()
        message_id = a.sticker(sticker=player.game.cards.now.light).send()['result']['message_id']
        send_status(player.game, message_id)
        
@b.message('/stop0')
def stop_game(a):
    if g.del_game(a.data['chat']['id']):
        a.msg('Игра была удалена').send()
    else:
        a.msg('Что удалять?').send()
        
@b.message(True)
def check_sticker(a):
    sticker = a.data.get('sticker')
    if sticker:
        sticker_id = sticker['file_id']
        player = g.get_player(a.data['from']['id'])
        if player:
            card = player.check_card(sticker_id)
            if card:
                player.game.put_card(card)
                old_message_id = player.game.message_id
                if len(player.cards) == 1:
                    a.msg('UNO!').send()
                elif not player.cards:
                    pl = g.del_player(player.id)
                    if pl:
                        a.msg('Победа <a href="tg://user?id={}">{}</a>!!!'.format(pl.id, pl.name), parse_mode='HTML').send()
                    if player.game.is_end():
                        a.msg('Конгры').send()
                        g.del_game(player.game.id)
                send_status(player.game, a.data['message_id'])
                clear_reply_markup(a.data['chat']['id'], old_message_id)
                
@b.callback_query('get')
def get_card(a):
    player = g.get_player(a.data['from']['id'])
    if is_norm(a, player) and not player.is_get_card:
        player.get_card()
        update_status(player.game)
    else:
        a.answer(text='Не трожь').send()

@b.callback_query('pass')
def pass_(a):
    player = g.get_player(a.data['from']['id'])
    if is_norm(a, player) and player.is_get_card:
        player.game.next()
        old_message_id = player.game.message_id
        send_status(player.game)
        clear_reply_markup(a.data['message']['chat']['id'], old_message_id)
    else:
        a.answer(text='Не трожь').send()

@b.inline_query('.?')
def my_card(a):
    player = g.get_player(a.data['from']['id'], True)
    if player:
        if player.game.play:
            cards = player.get_cards()
            result = []; i = 0
            desc = str(player.game)
            while i < len(cards):
                one = cards[i]
                if one['card']:
                    result.append(iqr(type='sticker', id=i, sticker_file_id=one['id']))
                else:
                    result.append(iqr(type='sticker', id=i, sticker_file_id=one['id'], input_message_content={'message_text': desc, 'parse_mode': 'HTML'}))
                i += 1
        else:
            result = [iqr(type='article', id=1, title='Игра не начата', input_message_content={'message_text': '/start0 что-бы начать'})]
    else:
        result = [iqr(type='article', id=1, title='Ты не в игре', input_message_content={'message_text': '/join0 что-бы зайти'})]
    a.answer(result, cache_time=0).send()

@app.route('/unohook', methods=['POST']) #Telegram should be connected to this hook
def webhook():
    b.check(request.get_json())
    #print(request.get_json())
    return 'ok', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
