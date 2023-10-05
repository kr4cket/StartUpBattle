<script>
export default {
  data() {
    return {

    }
  }
}
</script>

<template>
  <div class="header">
    <router-link to="/main" href="#" class="header__logo">
      <img src="../assets/header/logo.jpg" alt="Logo" class="header__logo logo">
    </router-link>
    <nav class="header__nav">
      <router-link to="/main" class="header__link">Главная</router-link>
      <router-link to="/vocabulary" class="header__link">Лексика</router-link>
      <router-link to="/grammar" class="header__link">Грамматика</router-link>
      <router-link to="/immersion" class="header__link">Погружение</router-link>
      <router-link to="/bot" class="header__link">Общение</router-link>
    </nav>
  </div>
</template>

<style scoped>
.header {
  display: flex;
  justify-content: center;
  gap: 3vw;
  align-items: center;
  padding-top: 30px;
  padding-bottom: 30px;
}

.header__logo {
  width: 75px;
  border-radius: 25%;
}
.header__nav {
  display: flex;
  gap: 3vw;
}
.header__link {
  display: inline-block;
  color: black;
  text-decoration: none;
}
</style>