import { ITodo } from "../types";
import TodoItem from "./TodoItem";
const TodoView = ({ todoList }: { todoList: ITodo[] }) => {
  return (
    <div>
      <ul>
        {todoList &&
          todoList?.length > 0 &&
          todoList.map((todo: ITodo) => <TodoItem todo={todo} />)}
      </ul>
    </div>
  );
};

export default TodoView;
