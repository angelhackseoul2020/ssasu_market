<template>
  <div class="adminUserAddWrap">
    <button id="close">X</button>
    <div id="adminUserAddLabel">
      <p id="userIdText">아이디</p>
      <p id="userNicknameText">닉네임</p>
      <p id="userEmailText">이메일</p>
      <p id="userTellText">연락처</p>
    </div>
    <div class="adminUserAdd">
      <input type="text" id="userId" placeholder="아이디" v-model="id" />
      <input type="text" id="userNickname" placeholder="닉네임" v-model="nick" />
      <input type="text" id="userEmail" placeholder="이메일" v-model="email" />
      <input type="text" id="userTell" placeholder="연락처" v-model="phone" />

      <div class="deleteSave">
        <button type="submit" id="delete">delete</button>
        <button type="submit" id="save">save</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "AdminUser",
  components: {},
  props: {
    person: {
      type: Object
    }
  },
  data() {
    return {
      id: "",
      nick: "",
      email: "",
      phone: ""
    };
  },
  mounted() {
    console.log(this.person);
    if (this.person) {
      this.id = this.person.id;
      this.nick = this.person.nick;
      this.email = this.person.email;
      this.phone = this.person.phone;
    }
    var close = document.getElementById("close");
    close.addEventListener("click", () => {
      this.$emit("close");
    });
    var save = document.getElementById("save");
    save.addEventListener("click", () => {
      axios.delete(
        "http://127.0.0.1:8000/accounts/myinfo/" +
          sessionStorage.getItem("id") +
          "/"
      );
    });
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  box-sizing: border-box;
}
#close {
  width: 30px;
  height: 30px;
  background-color: red;
  position: absolute;
  top: 10px;
  right: 10px;
}
.adminUserAddWrap {
  width: 80%;
  height: 70%;
  top: 15%;
  left: 10%;
  position: absolute;
  background-color: rgb(252, 252, 252);
  border-radius: 15px;
}
#adminUserAddLabel {
  position: absolute;
  width: 20%;
  height: 100%;
  left: 10%;
  top: 10%;
}
#userIdText {
  position: absolute;
  font-size: 40px;
  right: 0;
  top: 50px;
}
#userNicknameText {
  position: absolute;
  font-size: 40px;
  right: 0;
  top: 150px;
}
#userEmailText {
  position: absolute;
  font-size: 40px;
  right: 0;
  top: 250px;
}
#userTellText {
  position: absolute;
  font-size: 40px;
  right: 0;
  top: 350px;
}
.adminUserAdd {
  position: absolute;
  width: 65%;
  height: 100%;
  left: 35%;
  top: 10%;
}
#userId {
  position: absolute;
  top: 50px;
  left: 30px;
}
#userNickname {
  position: absolute;
  top: 150px;
  left: 30px;
}
#userEmail {
  position: absolute;
  top: 250px;
  left: 30px;
}
#userTell {
  position: absolute;
  top: 350px;
  left: 30px;
}
label {
  display: block;
  width: 100%;
  font-size: 12px;
  line-height: 16px;
}
input {
  width: 300px;
  height: 50px;
  font-size: 2rem;
  background-color: #fdafd063;
  border-radius: 20px;
  border: 1.2px solid rgba(245, 245, 245, 0.575);
}
input:focus,
input:hover,
input:active {
  outline: none;
  box-shadow: none;
  border-color: #f3c0d8;
}
button {
  width: 100px;
  height: 40px;
  font-size: 1.3rem;
  text-align: center;
  border-style: none;
  border-radius: 40px;
  cursor: pointer;
}
#delete {
  position: absolute;
  bottom: 90px;
  right: 220px;
  background-color: rgb(156, 4, 4);
}
#save {
  position: absolute;
  bottom: 90px;
  right: 100px;
  background-color: #26833d;
}
</style>