<script lang="ts">
  import { createEventDispatcher } from "svelte";

  import { postTodo } from "@/api";

  const dispatch = createEventDispatcher();

  let newTitle: string = "";
  let isUpdating = false;

  const addTodo = async () => {
    isUpdating = true;

    const ok = await postTodo({
      title: newTitle,
      done: false,
    });

    if (ok) {
      newTitle = "";
    }

    isUpdating = false;

    dispatch("save");
  };
</script>

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
