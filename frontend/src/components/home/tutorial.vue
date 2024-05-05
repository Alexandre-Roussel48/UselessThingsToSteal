<script>

export default {
  name: 'home_tutorial',
  data () {
    return {
      num : 1
    }
  },
  methods: {
    left () {
      if (this.num > 1) {
        this.num -= 1;
      }
    },
    right () {
      if (this.num < 7) {
        this.num += 1;
        if (this.num==7) {
          this.$store.commit('disable_tutorial');
        }
      }
    }
  }
}

</script>

<template>
  <nav class="navbar has-background-info">
    <div class="navbar-brand">
      <div class="navbar-item">
        <img class="header_logo invisible" src="@/assets/favicon.svg">
      </div>
    </div>
    <div class="navbar-menu">
      <div class="navbar-start" v-if="this.num==2">
        <div class="navbar-item">
          <img class="header_category pulsate" src="@/assets/tutorial/large_arrow.svg">
        </div>
      </div>
      <div class="navbar-start" v-if="this.num==5">
        <div class="navbar-item">
          <img class="header_category invisible" src="@/assets/tutorial/large_arrow.svg">
        </div>
        <div class="navbar-item">
          <img class="header_category pulsate" src="@/assets/tutorial/little_arrow.svg">
        </div>
      </div>
      <div class="navbar-end" v-if="this.num==3">
        <div class="navbar-item">
          <img class="header_category pulsate" src="@/assets/tutorial/little_arrow.svg">
        </div>
        <div class="navbar-item">
          <img class="header_category invisible" src="@/assets/drop.svg">
        </div>
        <div class="navbar-item">
          <img class="header_category invisible" src="@/assets/me.svg">
        </div>
        <div class="navbar-item">
          <button class="button is-success invisible">
            <span>Log out</span>
          </button>
        </div>
      </div>
      <div class="navbar-end" v-if="this.num==4">
        <div class="navbar-item">
          <img class="header_category pulsate" src="@/assets/tutorial/little_arrow.svg">
        </div>
        <div class="navbar-item">
          <img class="header_category invisible" src="@/assets/me.svg">
        </div>
        <div class="navbar-item">
          <button class="button is-success invisible">
            <span>Log out</span>
          </button>
        </div>
      </div>
    </div>
  </nav>
  <div class="modal is-active">
    <div class="modal-content">
      <div class="box">
        <h3 class="title">HELLO 👋</h3>
        <p class="content">
          Step into the world of card hustlin' and street swipes! In this app, you're about to hustle your way to the sickest card collection while dodging those trying to snag your stash.
        </p>
        <div class="columns">
          <div class="column is-10 is-offset-1">
            <div class="columns is-vcentered">
              <div class="column is-1">
                <button class="button is-large" v-on:click.prevent="left()">
                  <span class="icon is-medium">
                    <font-awesome-icon :icon="['fas', 'caret-left']" />
                  </span>
                </button>
              </div>
              <div class="column is-10" v-if="this.num==1">
                <div class="box">
                  <h4 class="title is-4">Gettin' Started 🫠</h4>
                  <p class="content">
                    When you sign up, you're rollin' with 5 basic cards. They're your starter pack, homie. Time to make 'em shine.
                  </p>
                </div>
              </div>
              <div class="column is-10" v-if="this.num==2">
                <div class="box">
                  <h4 class="title is-4">Your Loot 🤑</h4>
                  <p class="content">
                    Hit up your inventory to peep your collection. See what you've copped so far, sorted by rarity. Keep an eye on what's up for grabs.
                  </p>
                </div>
              </div>
              <div class="column is-10" v-if="this.num==3">
                <div class="box">
                  <h4 class="title is-4">Swipe Game 🥷</h4>
                  <p class="content">
                    Feelin' bold? Every 10 mins, you can swipe a random card from some other player. Watch your back, though - they might come for you too!
                  </p>
                </div>
              </div>
              <div class="column is-10" v-if="this.num==4">
                <div class="box">
                  <h4 class="title is-4">Score Drops 💵</h4>
                  <p class="content">
                    Every 5 mins, you're in for a drop - a chance to score a fresh basic card. Keep hustlin' and stacking those cards.
                  </p>
                </div>
              </div>
              <div class="column is-10" v-if="this.num==5">
                <div class="box">
                  <h4 class="title is-4">Vault Protection 🔒</h4>
                  <p class="content">
                    Keep your rarest cards safe in your vault. You can stash one card of each rarity there. Keep it locked down tight, playa.
                  </p>
                </div>
              </div>
              <div class="column is-10" v-if="this.num==6">
                <div class="box">
                  <h3 class="title">Ready to Roll ?</h3>
                  <p class="content">
                    Now that you know the deal, it's time to hit the streets. Start stacking cards, dodging swipes, and become the king of the hustle!
                  </p>
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