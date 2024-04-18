<script>

export default {
  name: 'home_login',
  data () {
    return {
      username: "",
      password: "",
      status: ""
    }
  },
  methods: {
    login() {
      fetch(`${this.$url_prefix}/login`, {
        method: 'POST',
        headers: {
          'Content-Type':'application/json'
        },
        body: JSON.stringify({
          'username':this.username,
          'password':this.password
        })
      })
      .then(resp => resp.json())
      .then(data => {
        if ('status' in data) {
          this.status = data['status'];
        } else {
          this.$store.commit('set_user_data', {
            username: this.username,
            token: data['token']
          });
        }
      });
    }
  },
  computed: {
    can_login () {
      return this.password != "" && this.username != "";
    }
  }
}

</script>

<template>
  <div class="box">
    <div class="field">
      <p class="control has-icons-left">
        <input class="input" type="text" placeholder="Username" v-model="username">
        <span class="icon is-small is-left">
          <font-awesome-icon :icon="['fas', 'user']" />
        </span>
        <span class="icon is-small is-right">
          <i class="fas fa-check"></i>
        </span>
      </p>
    </div>
    <div class="field">
      <p class="control has-icons-left">
        <input class="input" type="password" placeholder="Password" v-model="password">
        <span class="icon is-small is-left">
          <font-awesome-icon :icon="['fas', 'lock']" />
        </span>
      </p>
    </div>
    <div class="field">
      <small v-if="this.status != ''">{{this.status}}</small>
      <p class="control">
        <button class="button is-success" v-if="can_login" v-on:click.prevent="login()">
          Login
        </button>
        <button class="button is-success" disabled v-else>
          Login
        </button>
      </p>
    </div>
  </div>
</template>