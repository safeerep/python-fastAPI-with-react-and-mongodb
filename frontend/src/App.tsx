import { useEffect, useState } from "react";
import TodoView from "./components/TodoView";
import axios from "axios";
import { BASE_URL } from "./constants";
import toast, { Toaster } from "react-hot-toast";

function App() {
  const [todoList, setTodoList] = useState([
    // {
    //   title: "tea",
    //   description: "description"
    // },
    // {
    //   title: "tea",
    //   description: "description"
    // },
    // {
    //   title: "tea",
    //   description: "description"
    // }
  ]);
  const [title, setTitle] = useState("");
  const [desc, setDesc] = useState("");

  useEffect(() => {
    fetchTodos()
  }, []);

  const fetchTodos = () => {
    axios.get(`${BASE_URL}/get-todos`).then((res) => {
      setTodoList(res.data?.todos);
    });
  }

  const addTodoHandler = () => {
    axios
      .post(`${BASE_URL}/create-todo`, {
        title: title,
        description: desc,
      })
      .then((res) => {
        if(res) {
          toast.success("successfully added new todo")
          fetchTodos()
        }
      });
  };
  return (
    <>
      <div className="justify-center mx-auto w-[400px] bg-green-400 mt-4 p-6">
        <h1 className="mb-1 w-full text-center font-bold text-black">
          TASK MANAGER
        </h1>
        <h1 className="mb-3 w-full text-center font-bold text-black">
          FASTAPI - React - MongoDB
        </h1>

        <div className="bg-gray-200 p-3 flex flex-col justify-center">
          <h5 className="bg-black p-2 text-white mb-3">Add Your Task</h5>
          <input
            className="mb-2 p-3 border border-black w-full"
            onChange={(event) => setTitle(event.target.value)}
            placeholder="Title"
          />
          <br />
          <input
            className="mb-2 p-3 border border-black w-full"
            onChange={(event) => setDesc(event.target.value)}
            placeholder="Description"
          />
          <br />
          <div className="w-full flex justify-center">
            <button
              className=" mb-3 font-semibold bg-rose-500 hover:bg-red-600 p-3 rounded-md"
              onClick={addTodoHandler}
            >
              Add Task
            </button>
          </div>
          <h5 className="bg-black p-2 text-white mb-3">Your Tasks</h5>
          <div>
            <TodoView updateTodos={fetchTodos} todoList={todoList} />
          </div>
        </div>
        <h6 className="card text-dark bg-warning py-1 mb-0">
          Copyright 2024, All rights reserved &copy; safeerep
        </h6>
      </div>
      <Toaster />
    </>
  );
}

export default App;
