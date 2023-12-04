<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4 mt-5">
                <h1 class="title">Faça o seu cadastro!</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Nome</label>
                        <div class="control">
                            <input type="text" class="input" v-model="state.username">
                        </div>
                    </div>
                    <div class="field">
                        <label>CPF/CNPJ</label>
                        <div class="control">
                            <input type="text" class="input" v-model="state.cpfCnpj">
                        </div>
                    </div>
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
                        <label>É Lojista?</label>
                        <div class="control">
                            <input type="checkbox" class="checkbox" v-model="state.isShopKeeper">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Cadastrar</button>
                        </div>
                    </div>

                    Ou <router-link to="/log-in">Clique aqui</router-link> para entrar!
                </form>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { reactive } from 'vue';
import Swal from 'sweetalert2';

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  withCredentials: true,
  headers: {
    Accept: "application/json",
    'Content-Type': "application/json",
  },
});

interface State {
    username: string;
    cpfCnpj: string;
    email: string;
    password: string;
    isShopKeeper: boolean;
}

const state: State = reactive( {
    username: '',
    cpfCnpj: '',
    email: '',
    password: '',
    isShopKeeper: false,
})

function submitForm() {
    const newUser = {
    username: state.username,
    cpf_cnpj: state.cpfCnpj,
    email: state.email,
    password: state.password,
    is_shopkeeper: state.isShopKeeper,
  }
    instance.post("api/v1/users/", newUser)
    .then((res) => {
        console.log(res);
        if (res.status !== 200) {
            Swal.fire({
                title: "Cadastro não realizado!",
                text: "Tente novamente!",
                icon: "error"
            });
        } else {
            Swal.fire({
                title: "Cadastro realizado!",
                text: "Agora você já pode usar a plataforma!",
                icon: "success"
            });
        }
    })
    resetFields()
}

function resetFields() {
    state.username = '',
    state.cpfCnpj = '',
    state.email = '',
    state.password = '',
    state.isShopKeeper = false
}

</script>


<style lang="scss">
@import '../../node_modules/bulma/css/bulma.min.css';
</style>
