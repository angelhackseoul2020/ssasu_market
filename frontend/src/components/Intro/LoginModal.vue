<template>
  <div>
    <div id="login-modal-back" :style="{ width: width + 'px', height: height + 'px' }"></div>
    <div id="login-modal">
      <div id="login-id-text">아이디</div>
      <input id="login-id-input" type="text" placeholder="아이디" v-model="id" />
      <div id="login-pw-text">비밀번호</div>
      <input id="login-pw-input" type="password" placeholder="비밀번호" v-model="pw" />
      <div id="login-submit">로그인</div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: {
    width: {
      type: Number
    },
    height: {
      type: Number
    }
  },
  data() {
    return {
      id: "",
      pw: ""
    };
  },
  mounted() {
    var submit = document.getElementById("login-submit");
    submit.addEventListener("click", () => {
      axios
        .post("http://127.0.0.1:8000/accounts/api-token-auth/", {
          userid: this.id,
          password: this.pw
        })
        .then(response => {
          console.log(response);
          if (response.status === 200) {
            sessionStorage.setItem("token", response.data.token);
            axios
              .get("http://127.0.0.1:8000/accounts/myinfo/" + this.id + "/")
              .then(response => {
                sessionStorage.setItem("id", response.data.id);
                location.href = "maps";
              });
          }
        });
    });
    var loginModal = document.getElementById("login-modal");
    loginModal.style.top = this.height / 2 - 200 + "px";
    loginModal.style.left = this.width / 2 - 400 + "px";
    var loginBack = document.getElementById("login-modal-back");
    loginBack.addEventListener("click", () => {
      this.$emit("closeLoginModal");
    });
  }
};
</script>

<style scoped>
input:focus,
input:hover,
input:active {
  outline: none;
  box-shadow: none;
}
#login-modal-back {
  position: absolute;
  opacity: 0.96;
  top: 0;
  left: 0;
}
#login-modal {
  position: absolute;
  width: 800px;
  height: 400px;
  background-color: white;
  border-radius: 30px;
  z-index: 1;
}
#login-id-text {
  position: absolute;
  width: 200px;
  height: 70px;
  font-size: 50px;
  padding: 10px 0;
  text-align: end;
  top: 50px;
  left: 100px;
}
#login-pw-text {
  position: absolute;
  width: 200px;
  height: 70px;
  font-size: 50px;
  padding: 10px 0;
  text-align: end;
  top: 150px;
  left: 100px;
}
#login-id-input {
  position: absolute;
  width: 330px;
  height: 70px;
  border: none;
  font-size: 50px;
  background: #ffdddd;
  border-radius: 25px;
  padding-left: 25px;
  top: 60px;
  left: 350px;
}
#login-pw-input {
  position: absolute;
  width: 330px;
  height: 70px;
  border: none;
  font-size: 50px;
  background: #ffdddd;
  border-radius: 25px;
  padding-left: 25px;
  top: 160px;
  left: 350px;
}
#login-submit {
  position: absolute;
  width: 160px;
  height: 70px;
  font-size: 40px;
  text-align: center;
  padding-top: 8px;
  background-color: #ffdddd;
  border-radius: 40px;
  left: 320px;
  top: 300px;
  cursor: pointer;
}
#login-submit:hover {
  background-color: #eba0ac;
}
</style>
