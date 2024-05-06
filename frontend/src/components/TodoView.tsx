import { ITodo } from "../types";
import TodoItem from "./TodoItem";
const TodoView = ({ todoList, updateTodos }: { todoList: ITodo[], updateTodos: any }) => {
  return (
    <div>
      <ul>
        {todoList &&
          todoList?.length > 0 &&
          todoList.map((todo: ITodo) => <TodoItem updateTodos={updateTodos} todo={todo} />)}
      </ul>
    </div>
  );
};

export default TodoView;
