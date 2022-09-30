# -*- coding: utf-8 -*-

import helpers.KeyManager as KeyManager

if __name__ == "__main__":
    app_id, secret_key = KeyManager.get_secret_key('2930f2f11f484eabbcb0cff2600874db')
    print('app_id    : {}\nsecret_key: {}'.format(app_id, secret_key))