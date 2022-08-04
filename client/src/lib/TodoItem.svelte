<script type="ts">
  import { delTodo, patchTodoDone } from "@/api";
  import type Todo from "@/interfaces/Todo";
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  export let todo: Todo;
  let isUpdating = false;

  const handleChangeDone = async (e: Event) => {
    isUpdating = true;

    const done = (e.target as HTMLInputElement).checked;

    const ok = await patchTodoDone({
      id: todo.id,
      done,
    });

    if (!ok) {
      todo.done = !done;
    }

    isUpdating = false;
    dispatch("changeDone");
  };

  const remove = async () => {
    isUpdating = true;
    await delTodo({
      id: todo.id,
    });

    dispatch("remove");
  };
</script>

{#if isUpdating}
  <div>...updating</div>
{:else}
  <div>
    <input
      id={`todo-item=${todo.id}`}
      type="checkbox"
      checked={todo.done}
      on:change|preventDefault={handleChangeDone}
    />
    <label for={`todo-item=${todo.id}`}>
      {#if todo.done}
        <del>{todo.title}</del>
      {:else}
        <span>{todo.title}</span>
      {/if}
    </label>
    <button on:click={remove}>X</button>
  </div>
{/if}

<style>
</style>
