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
      fetch(`${this.$url_prefix}/api/login`, {
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
        if ('token' in data) {
          this.$store.commit('set_user_data', {
            username: this.username,
            token: data['token'],
            connection_count: data['connection_count']
          });
          this.$store.commit('set_next_card', {next_card: data['next_card']});
          this.$store.commit('set_next_theft', {next_theft: data['next_theft']});
          this.$store.commit('set_thefts', {thefts: data['thefts']});
          const ws = new WebSocket(`${this.$ws_prefix}?authorization=${data['token']}`);

          ws.onopen = () => {
            this.$store.commit('set_websocket', ws);
          };

          ws.onmessage = (event) => {
            const jsonData = JSON.parse(event.data);
            const thefts = [];
            thefts.push(jsonData);
            this.$store.commit('set_thefts', {thefts: thefts});
          };

          ws.onclose = async () => {
            await fetch(`${this.$url_prefix}/api/user/set_last_connection`, {
              method: 'POST',
              headers: {
                'Content-Type':'application/json',
                'authorization': 'Bearer ' + this.$store.state.token
              }
            });
          };
        } else {
          this.status = data['status'];
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
          <span>Login</span>
        </button>
        <button class="button is-success" disabled v-else>
          <span>Login</span>
        </button>
      </p>
    </div>
  </div>
</template>