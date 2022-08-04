<script type="ts">
  import { getTodo, postTodo } from "@/api";

  import type Todo from "@/interfaces/Todo";
  import TodoItem from "@/lib/TodoItem.svelte";

  let newTitle: string = "";
  let todosPromise: Promise<Todo[]> = getTodo();

  let isUpdating = false;

  const refetch = () => {
    todosPromise = getTodo();
  };

  const addTodo = async () => {
    isUpdating = true;

    const ok = await postTodo({
      title: newTitle,
      done: false,
    });

    if (ok) {
      newTitle = "";
    }

    refetch();
    isUpdating = false;
  };
</script>

<h1>TODO LIST</h1>

<section style="height: 500px;">
  {#await todosPromise}
    <div>...loading</div>
  {:then todos}
    {#if todos.length > 0}
      {#each todos as todo}
        <TodoItem {todo} on:changeDone={refetch} on:remove={refetch} />
      {/each}
    {:else}
      <div>NO DATA</div>
    {/if}
  {:catch error}
    <div>{error}</div>
  {/await}
</section>

{#if isUpdating}
  <div>...updating</div>
{:else}
  <section>
    <form on:submit|preventDefault={addTodo}>
      <input bind:value={newTitle} />
      <button type="submit">ADD</button>
    </form>
  </section>
{/if}

<style>
</style>
