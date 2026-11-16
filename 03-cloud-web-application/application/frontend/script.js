const taskList = document.querySelector("#task-list");
const taskForm = document.querySelector("#task-form");
const message = document.querySelector("#message");

async function loadTasks() {
  const response = await fetch("/api/tasks");
  if (!response.ok) throw new Error("Unable to load tasks");
  const tasks = await response.json();
  taskList.replaceChildren();

  if (tasks.length === 0) {
    const empty = document.createElement("p");
    empty.textContent = "No tasks yet. Add your first task above.";
    taskList.append(empty);
    return;
  }

  for (const task of tasks) {
    const card = document.createElement("article");
    card.className = "task";

    const title = document.createElement("h3");
    title.textContent = task.title;

    const description = document.createElement("p");
    description.textContent = task.description || "No description";

    const status = document.createElement("small");
    status.textContent = `Status: ${task.status}`;

    const actions = document.createElement("div");
    actions.className = "task-actions";

    const complete = document.createElement("button");
    complete.type = "button";
    complete.textContent = "Mark completed";
    complete.addEventListener("click", async () => {
      const result = await fetch(`/api/tasks/${task.id}`, {
        method: "PATCH",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({status: "Completed"})
      });
      if (result.ok) await loadTasks();
    });

    const remove = document.createElement("button");
    remove.type = "button";
    remove.className = "secondary";
    remove.textContent = "Delete";
    remove.addEventListener("click", async () => {
      const result = await fetch(`/api/tasks/${task.id}`, {method: "DELETE"});
      if (result.ok) await loadTasks();
    });

    actions.append(complete, remove);
    card.append(title, description, status, actions);
    taskList.append(card);
  }
}

taskForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  message.textContent = "";

  const response = await fetch("/api/tasks", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      title: taskForm.elements.title.value,
      description: taskForm.elements.description.value
    })
  });

  if (!response.ok) {
    message.textContent = "Could not create task. Check the title and try again.";
    return;
  }

  taskForm.reset();
  message.textContent = "Task created successfully.";
  await loadTasks();
});

document.querySelector("#refresh").addEventListener("click", () => {
  loadTasks().catch(() => { message.textContent = "Unable to load tasks."; });
});

loadTasks().catch(() => { message.textContent = "Unable to connect to the application."; });
