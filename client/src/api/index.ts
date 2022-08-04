import type Todo from "@/interfaces/Todo";
import { sleep } from '@/utils/time';

const API_SPEED = 1000;
const _db = {
  todos: [
    {
      id: 1,
      title: "잠자기",
      done: true,
    },
    {
      id: 2,
      title: "공부하기",
      done: false,
    },
  ],
}

type GetTodo = () => Promise<Todo[]>
export const getTodo: GetTodo = async () => {
  await sleep(API_SPEED);

  return _db.todos;
};

type PostTodo = (todo: Pick<Todo, 'title' | 'done'>) => Promise<boolean>
export const postTodo: PostTodo = async (todo) => {
  await sleep(API_SPEED);

  const lastTodoId = _db.todos[_db.todos.length - 1]?.id || -1;

  _db.todos.push({
    id: lastTodoId + 1,
    title: todo.title,
    done: todo.done,
  });
  
  return true;
};

type PatchTodoDone = (todo: Pick<Todo, 'id' | 'done'>) => Promise<boolean>;
export const patchTodoDone: PatchTodoDone = async (todo) => {
  await sleep(API_SPEED);

  const finded = _db.todos.find(_todo => _todo.id === todo.id);
  if (finded) {
    finded.done = todo.done;
    return true;
  } else {
    return false;
  }
}

type DelTodo = (todo: Pick<Todo, 'id'>) => Promise<boolean>;
export const delTodo: DelTodo = async (todo) => {
  await sleep(API_SPEED);

  const findedIndex = _db.todos.findIndex(_todo => _todo.id === todo.id);
  if (findedIndex !== -1) {
    _db.todos.splice(findedIndex);
    return true;
  } else {
    return false;
  }
}