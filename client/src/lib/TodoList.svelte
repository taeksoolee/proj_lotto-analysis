<script type="ts">
  import { getTodo, postTodo } from "@/api";

  import type Todo from "@/interfaces/Todo";
  import TodoItem from "@/lib/TodoItem.svelte";
  import TodoAddForm from "@/lib/TodoAddForm.svelte";

  let todosPromise: Promise<Todo[]> = getTodo();

  const refetch = () => {
    todosPromise = getTodo();
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

<TodoAddForm on:save={refetch} />

<style>
</style>
