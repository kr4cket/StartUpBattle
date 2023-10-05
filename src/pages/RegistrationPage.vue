<script>
export default {
  data () {
    return {
      firstName: "",
      lastName: "",
      email: "",
      password: "",
      password_confirmation: "",
    }
  }
}
</script>

<template>
  <router-link to="/">Назад</router-link>
<div class="registration-title">Регистрация</div>
  <form id="registration-form">
    <input
        name="firstName"
        type="text"
        placeholder="Ваше имя"
        required
        v-model.trim="firstName"
    >
    <input
        name="lastName"
        type="text"
        placeholder="Ваша фамилия"
        required
        v-model.trim="lastName"
    >
    <input
      name="email"
      type="email"
      placeholder="Ваш email"
      required
      v-model.trim="email"
    >
    <input
        name="password"
        type="password"
        placeholder="Придумайте пароль"
        required
        v-model.trim="password"
    >
    <input
        name="password"
        type="password"
        placeholder="Повторите пароль"
        required
        v-model.trim="password_confirmation"
    >
    <button type="submit">Зарегистрироваться</button>
  </form>
</template>

<style>

</style>