<template>
  <div class="code-match">
    <div class="code-column">
      <h3>Python</h3>
      <pre><code>{{ python }}</code></pre>
    </div>
    <div class="code-column">
      <h3>JavaScript</h3>
      <pre><code>{{ javascript }}</code></pre>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  python: {
    type: String,
    required: true
  },
  javascript: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.code-match {
  display: flex;
  gap: 1rem;
}
.code-column {
  flex: 1;
}
pre {
  background: #f5f5f5;
  padding: 0.5rem;
  overflow: auto;
}
</style>
