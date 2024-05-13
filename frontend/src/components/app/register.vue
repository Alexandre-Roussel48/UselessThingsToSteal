<script>

export default {
  name: 'home_register',
  data () {
    return {
      username: "",
      password: "",
      password_check: "",
      status: ""
    }
  },
  methods: {
    register() {
      fetch(`${this.$url_prefix}/api/register`, {
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
          this.username = "";
          this.password = "";
          this.password_check = "";
          this.status = data['status'];
        }
      });
    }
  },
  computed: {
    can_register () {
      return this.password != "" && this.password_check != "" && this.username != "" && this.password == this.password_check;
    },
    password_class () {
      if (this.password != "" && this.password_check != "") {
        if (this.password == this.password_check) {
          return 'is-success';
        }
        return 'is-danger';
      }
      return '';
    }
  },
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
        <input class="input" :class="password_class" type="password" placeholder="Password" v-model="password">
        <span class="icon is-small is-left">
          <font-awesome-icon :icon="['fas', 'lock']" />
        </span>
      </p>
    </div>
    <div class="field">
      <p class="control has-icons-left">
        <input class="input" :class="password_class" type="password" placeholder="Password check" v-model="password_check">
        <span class="icon is-small is-left">
          <font-awesome-icon :icon="['fas', 'lock']" />
        </span>
      </p>
    </div>
    <div class="field">
      <small v-if="this.status != ''">{{this.status}}</small>
      <p class="control">
        <button class="button is-success" v-if="can_register" v-on:click.prevent="register()">
          Register
        </button>
        <button class="button is-success" disabled v-else>
          Register
        </button>
      </p>
    </div>
  </div>
</template>