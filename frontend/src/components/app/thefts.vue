<script>

export default {
  name: 'home_thefts',
  data () {
    return {
      num : 0,
      thefts : []
    }
  },
  methods: {
    left () {
      if (this.num > 0) {
        this.num -= 1;
      }
    },
    right () {
      if (this.num < this.thefts.length) {
        this.num += 1;
        if (this.num==this.thefts.length) {
          this.$store.commit('set_thefts', {thefts: []});
        }
      }
    }
  },
  mounted () {
    this.thefts = this.$store.getters.get_thefts;
  }
}

</script>

<template>
  <div class="modal is-active">
    <div class="modal-content" v-if="this.thefts.length > 0">
      <div class="box">
        <div class="columns">
          <div class="column is-10 is-offset-1">
            <div class="columns is-vcentered">
              <div class="column is-1 is-offset-3">
                <button class="button is-large" v-on:click.prevent="left()">
                  <span class="icon is-medium">
                    <font-awesome-icon :icon="['fas', 'caret-left']" />
                  </span>
                </button>
              </div>
              <div class="column is-4">
                <p class="thief_display">Stole by {{this.thefts[this.num]['thief']}}</p>
                <div class="card">
                  <div class="card-image">
                    <figure class="image">
                      <img :src="'src/assets/cards/' + this.thefts[this.num]['card']['name'] + '.png'" alt="Card image"/>
                    </figure>
                  </div>
                </div>
              </div>
              <div class="column is-1">
                <button class="button is-large" v-on:click.prevent="right()">
                  <span class="icon is-medium">
                    <font-awesome-icon :icon="['fas', 'caret-right']" />
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>