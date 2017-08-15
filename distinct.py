import os
import load_FromExcel
from xpinyin import Pinyin
import json


def main(filename_list, output_name='distinct-accounts.csv'):
    # filename_list = ['account-list-pingtuan.csv', 'account-list-miaosha.csv', 'account-list-tuangou.csv']
    # output_name = 'distinct.csv'
    account_dic = {}
    try:
        for filename in filename_list:
            with open(filename, 'r', encoding='utf-8', newline='\n') as f:
                column_count = 0
                for i in f.readlines():
                    dictionary = json.loads(i)
                    account_dic[dictionary['name']] = dictionary['url']
                    # account_dic[i.split(",")[0]] = i.split(",")[1][:-3]
                    # print(account_dic[i.split(",")[0]])
                    column_count += 1
                    # account_set.add(column)
                # print(column_count)
        print(len(account_dic))
        raycop = load_FromExcel.load('Raycop.xlsx')
        for row in raycop:
            # if row[0] is not None:
            #     row[0] = row[0].encode('unicode_escape').decode('utf-8')
            #     print(row[0])
            if row[0] in account_dic:
                del account_dic[row[0]]
        print(len(account_dic))
        with open(output_name, 'a', encoding='utf-8', newline='\n') as o:
            for key in account_dic.keys():
                t = {'name': key, 'url': account_dic[key]}
                o.writelines(json.dumps(t) + "\n")
                # o.writelines("'{'name':'%s', 'url':'%s'}'\n" % (key, account_dic[key]))
        return account_dic
    except Exception:
        print("Unexpected error:", sys.exc_info()[0])
    else:
        print("Distinct unsucceed")


if __name__ == '__main__':
    main()
