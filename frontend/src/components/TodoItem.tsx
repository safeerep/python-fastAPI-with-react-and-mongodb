import axios from "axios";
import { ITodo } from "../types";
import { BASE_URL } from "../constants";

const TodoItem = ({ todo }: { todo: ITodo }) => {
  const deleteTodoHandler = (title: string) => {
    axios
      .delete(`${BASE_URL}/remove-todo/${title}`)
      .then((res) => console.log(res.data));
  };
  return (
    <div className="bg-cyan-400 border-black border flex justify-between mt-2 text-center p-2">
      <p>
        <span className="font-bold underline">{todo.title} : </span>{" "}
        {todo.description}
      </p>
      <button
        onClick={() => deleteTodoHandler(todo.title)}
        className="bg-red-600 px-3 rounded-md justify-end"
      >
        X
      </button>
    </div>
  );
};

export default TodoItem;
