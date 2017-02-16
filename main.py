import os
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://sb-app:1HrPKFkA@104.131.74.163:27172/status-board')
db = client['status-board']


def main():
    users = db.users.find(
        {'roles': 'hacker'},
        {'profile.resume': 1, 'profile.name': 1, 'profile.school': 1, 'profile.graduating': 1}
    )
    count = 0
    for user in users:
        print(user['profile']['name'])
        out_dir = 'output/' + user['profile']['school'].strip()
            # str(user['profile']['graduating'])
        try:
            if (not os.path.exists(out_dir)):
                os.makedirs(out_dir)
            raw_resume = user['profile']['resume']
            if (raw_resume != ''):
                with open(out_dir + '/' + user['profile']['name'] + '.pdf', 'wb+') as f:
                    f.write(raw_resume)
            count += 1
        except Exception as e:
            print(e)
    print(count)

if __name__ == '__main__':
    main()
    client.close()
