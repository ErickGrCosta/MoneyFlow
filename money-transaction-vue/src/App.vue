<template>
  <div id="wrapper">
    <nav class="navbar is-dark is-fixed-top">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong class="has-text-white">Money Transaction</strong>
        </router-link>
        
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="state.showMobileMenu = !state.showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu is-flex is-flex-wrap-wrap is-flex-direction-column is-align-content-flex-end" id="navbar-menu" :class="{'is-active': state.showMobileMenu}">
    
        <div class="navbar-start">

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">Log in</router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view></router-view>
    </section>
    
    
    <footer class="footer">
      <p class="has-text-centered">Money Transaction (c) 2023</p>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive } from 'vue'

interface State {
  inputText: string;
  showMobileMenu: boolean;
  modalClicked: boolean;
  isAuthenticated: boolean;
  token: string | null;
  isLoading: boolean;
}

const state:State = reactive({
  inputText: '',
  showMobileMenu: false,
  modalClicked: false,
  isAuthenticated: false,
  token: '',
  isLoading: false,
})  

onMounted(() => {
  if(localStorage.getItem('token')) {
    state.token = localStorage.getItem('token')
    state.isAuthenticated = true
  } else {
    state.token = ''
    state.isAuthenticated = false
  }
  setToken(state.token)
})

function setToken(token:any) {
  state.token = token
  state.isAuthenticated = true
}

// function removeToken(state) {
//   state.token = ''
//   state.isAuthenticated = false
// }

</script>

<style lang="scss">
@import '../node_modules/bulma/css/bulma.min.css';
</style>
