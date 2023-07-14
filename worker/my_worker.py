import redis
import json

r = redis.StrictRedis(
    host='localhost',
    port=6379,
    decode_responses=True,
)


def get_data(file_id):
    result = None
    task_list = json.loads(r.get('task_list'))
    if task_list[file_id][0].__class__ == int:
        result = task_list[file_id][0]
        r.set('task_list', json.dumps(task_list))
    return result


def set_task(file_id, st, word_len):
    task_list = json.loads(r.get('task_list'))
    task_list[file_id] = (st, word_len)
    r.set('task_list', json.dumps(task_list))


if __name__ == '__main__':
    r.set('task_list', json.dumps({}))
    # print(r.rpop('new'))
    print("worker running")
    while True:
        task_list = json.loads(r.get('task_list'))
        for task in task_list.values():
            if task[0].__class__ == int:continue
            count = 0
            for word in  task[0].split(sep=' '):
                count+=1 if len(word)==task[1] else 0
            task[0] = count

        r.set('task_list', json.dumps(task_list))
