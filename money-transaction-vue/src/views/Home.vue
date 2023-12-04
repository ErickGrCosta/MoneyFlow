<template>
    <div class="section is-flex is-justify-content-center">
      Bem vindo {{ 'usuario' }}!
    </div>
    <div class="section is-flex is-justify-content-center">
      Saldo: R${{ 'amount' }}
    </div>

    <!-- <div v-if="!state.is_shopkeeper"></div> -->

    <div class="section is-flex is-justify-content-center">
      <button class="button is-success is-large modal-button" data-target="modal" aria-haspopup="true" @click="state.modalClicked = true"><i class="fa-solid fa-money-bill-transfer mr-2"></i>Transferir
      </button>    
    </div>
    <div class="modal" :class="{'is-active': state.modalClicked}">
      <div class="modal-background" @click="state.modalClicked = false"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Transferência</p>
          <button class="delete" aria-label="close" @click="state.modalClicked = false"></button>
        </header>
        <section class="modal-card-body">
          <label for="cpf">CPF/CNPJ:</label>
          <input class="input mb-2" v-model="state.formFields.cpfCnpj" type="text" id="cpf"/>
          <label for="amount">Valor:</label>
          <input class="input mb-2" v-model="state.formFields.amount" type="number" id="amount"/>
        </section>
        <footer class="modal-card-foot">
          <button class="button is-success">Transferir</button>
          <button class="button" @click="state.modalClicked = false">Cancel</button>
        </footer>
      </div>
    </div>

</template>

<script setup lang="ts">
import { onMounted, reactive } from 'vue'
import axios from 'axios'
// import Swal from 'sweetalert2'


interface State {
  inputText: string;
  showMobileMenu: boolean;
  modalClicked: boolean;
  formFields: {
    cpfCnpj: string;
    amount: number; 
  }
}

const state: State = reactive({
  inputText: '',
  showMobileMenu: false,
  modalClicked: false,
  formFields: {
    cpfCnpj: '',
    amount: 0 
  }
})

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  withCredentials: true,
  headers: {
    Accept: "application/json",
    'Content-Type': "application/json",
  },
});

onMounted(() => {
  instance.get('api/v1/transactions/')
  .then((res) => {
    console.log(res);
  })
  .catch(error => {
    console.log(error);
  })
  console.log('oi');
  
}
)  

</script>

<style lang="scss">
@import '../../node_modules/bulma/css/bulma.min.css';
</style>
