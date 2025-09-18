import React, { useEffect, useState } from "react";

export const App = () => {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState("");
  const [editingTodo, setEditingTodo] = useState(null);
  const [editingText, setEditingText] = useState("");

  const API_BASE = "https://my-json-server.typicode.com/LukaVucinic/intezivna_ob/todos";

  // Fetch all todos on component mount
  useEffect(() => {
    fetchTodos();
  }, []);

  // Fetch all todos from the server
  const fetchTodos = async () => {
    const response = await fetch(API_BASE);
    if (!response.ok) throw new Error("Failed to fetch todos");
    const data = await response.json();
    setTodos(data);
  };

  // Add a new todo
  const handleAddTodo = async (e) => {
    e.preventDefault();
    if (!newTodo.trim()) return; // ignore empty strings
 
    const newItem = {
      id:Date.now(),
      text: newTodo.trim(),
    };

    const response = await fetch(API_BASE, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newItem),
    });

    if (!response.ok) throw new Error("Failed to add todo");
    
    const createdTodo = await response.json();
    setTodos([...todos, createdTodo]);
    setNewTodo("");
  };

  // Start editing an existing todo
  const handleEditClick = (todo) => {
    setEditingTodo(todo);
    setEditingText(todo.text);
  };

  // Save the edited todo
  const handleSaveEdit = async (id) => {
    const response = await fetch(`${API_BASE}/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ...editingTodo, text: editingText }),
    });

    if (!response.ok) throw new Error("Failed to update todo");
    
    const updatedTodo = await response.json();
    setTodos(todos.map(todo => (todo.id === id ? updatedTodo : todo)));
    setEditingTodo(null);
    setEditingText("");
  };

  // Delete a todo
  const handleDelete = async (id) => {
    const response = await fetch(`${API_BASE}/${id}`, {
      method: "DELETE",
    });

    if (!response.ok) throw new Error("Failed to delete todo");
  
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
          className="bg-blue-500 text-white px-4 py-1 rounded-r disabled:bg-blue-300"   
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
                  className="bg-green-500 text-white px-2 py-1 rounded mr-2 disabled:bg-green-300"
                >
                  Save
                </button>
                <button
                  onClick={() => setEditingTodo(null)}
                  className="bg-gray-500 text-white px-2 py-1 rounded disabled:bg-gray-300"
                >
                  Cancel
                </button>
              </>
            ) : (
              // Display mode
              <>
                <span className="mr-2 flex-1">{todo.text}</span>
                <button
                  onClick={() => handleEditClick(todo)}
                  className="bg-yellow-500 text-white px-2 py-1 rounded mr-2 disabled:bg-yellow-300"
                >
                  Edit
                </button>
                <button
                  onClick={() => handleDelete(todo.id)}
                  className="bg-red-500 text-white px-2 py-1 rounded disabled:bg-red-300"
                >
                  Delete
                </button>
              </>
            )}
          </div>
        ))}
      </div>
      
      {!todos.length && (
        <div className="text-center py-4 text-gray-500">
          No todos yet. Add your first todo!
        </div>
      )}
    </div>
  );
};