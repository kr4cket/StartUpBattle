<script>

</script>

<template>
  <div class="container">
    <router-view></router-view>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
html, body {
  height: 100%;
  font-family: 'Montserrat', sans-serif;
  font-size: 25px;
}
.container {
  max-width: 1600px;
  padding: 0 15px;
  margin: 0 auto;
}
input, button {
  font-family: 'Montserrat', sans-serif;
}
</style>
