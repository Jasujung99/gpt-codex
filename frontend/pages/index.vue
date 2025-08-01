<template>
  <div>
    <h1>CodeMatch Demo</h1>
    <CodeMatch :python="pythonExample" :javascript="javascriptExample" />
  </div>
</template>

<script setup>
const pythonExample = `def greet(name):
    print(f"Hello, {name}!")`
const javascriptExample = `function greet(name) {
  console.log('Hello, ' + name + '!');
}`
</script>
