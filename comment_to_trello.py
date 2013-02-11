# -*- coding:utf-8 -*-
# 
from trolly import client as trolly_client
from trolly import board as trolly_board
from trolly import card
from pprint import pprint

if __name__ == "__main__":
    import sys

    # apply r/w token from "https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user"
    [trello_key, trello_token, board_id, card_short_id, comment] = sys.argv[1:8]
    
    client = trolly_client.Client(trello_key, user_auth_token = trello_token)
    board = trolly_board.Board(client, board_id)
    card = board.getCard(card_short_id)
    card.addComments(comment)

