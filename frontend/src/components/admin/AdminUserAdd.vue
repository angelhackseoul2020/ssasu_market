<template>
  <div class="adminUserAddWrap">
    <div class="adminUserAdd">
      <form action method="GET">
        <label for="userId">아이디</label>
        <input type="text" id="userId" placeholder="아이디" required v-model="person.id"/>

        <label for="userNickname">닉네임</label>
        <input type="text" id="userNickname" placeholder="닉네임" />

        <label for="userEmail">이메일</label>
        <input type="text" id="userEmail" placeholder="이메일" />

        <label for="userTell">연락처</label>
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
.adminUserAdd {
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
  background-color: rgb(156, 4, 4);
}
#save {
  background-color: #26833d;
}
</style>