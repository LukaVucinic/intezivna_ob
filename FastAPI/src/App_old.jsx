import React, { useEffect, useState } from "react";

export const App = () => {
  const storedTodos = localStorage.getItem("todos");
  // 1. Load initial todos from Local Storage (or use an empty array if none)
  const [todos, setTodos] = useState(() => {
    return storedTodos ? JSON.parse(storedTodos) : [];
  });

  // States for new todo and editing
  const [newTodo, setNewTodo] = useState("");
  const [editingTodo, setEditingTodo] = useState(null);
  const [editingText, setEditingText] = useState("");

  // 2. Update Local Storage whenever `todos` changes
  useEffect(() => {
    localStorage.setItem("todos", JSON.stringify(todos));
  }, [todos]);

  // Add a new todo
  const handleAddTodo = e => {
    e.preventDefault();
    if (!newTodo.trim()) return; // ignore empty strings

    const newItem = {
      id: Date.now(),
      text: newTodo.trim(),
    };
    setTodos([...todos, newItem]);
    setNewTodo(""); // clear input
  };

  // Start editing an existing todo
  const handleEditClick = todo => {
    setEditingTodo(todo);
    setEditingText(todo.text);
  };

  // Save the edited todo
  const handleSaveEdit = id => {
    setTodos(
      todos.map(todo =>
        todo.id === id ? { ...todo, text: editingText } : todo
      )
    );
    setEditingTodo(null);
    setEditingText("");
  };

  // Delete a todo
  const handleDelete = id => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  return (
    <div className="max-w-xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Todo App</h1>

      {/* Form to add new todo */}
      <form onSubmit={handleAddTodo} className="mb-4 flex">
        <input
          type="text"
          placeholder="Enter todo..."
          value={newTodo}
          onChange={e => setNewTodo(e.target.value)}
          className="border border-gray-300 rounded-l px-2 py-1 w-3/4"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-1 rounded-r"
        >
          Add
        </button>
      </form>

      {/* List of todos */}
      <div>
        {todos.map(todo => (
          <div
            key={todo.id}
            className="border border-gray-300 p-2 mb-2 rounded flex items-center"
          >
            {editingTodo?.id === todo.id ? (
              // Edit mode
              <>
                <input
                  type="text"
                  value={editingText}
                  onChange={e => setEditingText(e.target.value)}
                  className="border border-gray-300 rounded px-2 py-1 mr-2 w-3/4"
                />
                <button
                  onClick={() => handleSaveEdit(todo.id)}
                  className="bg-green-500 text-white px-2 py-1 rounded mr-2"
                >
                  Save
                </button>
                <button
                  onClick={() => setEditingTodo(null)}
                  className="bg-gray-500 text-white px-2 py-1 rounded"
                >
                  Cancel
                </button>
              </>
            ) : (
              // Display mode
              <>
                <span className="mr-2 flex-1">{todo.text}:{todo.id}</span>
                <button
                  onClick={() => handleEditClick(todo)}
                  className="bg-yellow-500 text-white px-2 py-1 rounded mr-2"
                >
                  Edit
                </button>
                <button
                  onClick={() => handleDelete(todo.id)}
                  className="bg-red-500 text-white px-2 py-1 rounded"
                >
                  Delete
                </button>
              </>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};
