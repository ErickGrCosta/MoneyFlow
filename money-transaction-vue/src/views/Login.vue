<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4 mt-5">
                <h1 class="title">Faça o seu cadastro!</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" class="input" v-model="state.email">
                        </div>
                    </div>
                    <div class="field">
                        <label>Senha</label>
                        <div class="control">
                            <input type="password" class="input" v-model="state.password">
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Entrar</button>
                        </div>
                    </div>

                    Ou <router-link to="/log-in">Clique aqui</router-link> para entrar!
                </form>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

// import axios from 'axios'
import { onMounted, reactive } from 'vue'

interface State {
    email: string;
    password: string;
}

const state: State = reactive( {
    email: '',
    password: '',
})


onMounted(() => {
    document.title = 'Login'
})

function submitForm() {
    
}

</script>