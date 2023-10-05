<script>
export default {
  data () {
    return {
      email: '',
      password: '',
    }
  },
  methods: {
    formValidation() {
      if (this.email.value > 0 && this.password > 0) {
        return 0;
      }
    }
  }
}
</script>

<template>
  <router-link to="/">Назад</router-link>
  <div class="login-title">Войти</div>
  <form id="login-form" >
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
        placeholder="12345678"
        required
        v-model.trim="password"
    >
    <button type="submit" v-on:click="formValidation">Войти</button>
  </form>
</template>

<style>

</style>