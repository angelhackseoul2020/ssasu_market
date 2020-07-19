<template>
  <div class="adminUserAddWrap">
    <div id="adminUserAddLabel">
      <p id="userIdText">아이디</p>
      <p id="userNicknameText">닉네임</p>
      <p id="userEmailText">이메일</p>
      <p id="userTellText">연락처</p>
    </div>
    <div class="adminUserAdd">
      <form action method="GET">
        <label for="userId">아이디</label>
        <input type="text" id="userId" placeholder="아이디" required v-model="person.id"/>

        <label for="userNickname">닉네임</label>
        <input type="text" id="userNickname" placeholder="닉네임" />
        <input type="text" id="userEmail" placeholder="이메일" />
        <input type="text" id="userTell" placeholder="연락처" />

        <div class="deleteSave">
          <button type="submit" id="delete">delete</button>
          <button type="submit" id="save">save</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminUser",
  components: {},
  props:{
    person:{
      type:Object
    }
  },
  mounted(){
    console.log(this.person);
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  box-sizing: border-box;
}
.adminUserAddWrap {
  width: 60%;
  height: 70%;
  top: 15%;
  left: 20%;
  position:absolute;
  background-color: rgb(252, 252, 252);
  border-radius: 15px;

}
#adminUserAddLabel {
  position: absolute;
  width: 30%;
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
  width: 70%;
  height: 100%;
  left: 40%;
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
  bottom: 170px;
  right: 700px;
  background-color: rgb(156, 4, 4);
}
#save {
  position: absolute;
  bottom: 170px;
  right: 580px;
  background-color: #26833d;
}
</style>