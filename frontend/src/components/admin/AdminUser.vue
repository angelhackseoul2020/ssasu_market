<template>
  <div class="adminUserWrap">
    <button id="userAddBtn">유저 추가</button>
    <div id="userList">
      <row :uid="id" :nick="nick" :address="address" :reviewcnt="reviewcnt" />
      <row
        v-for="(user,index) in userList"
        :key="user.id"
        :index="index"
        :uid="user.userid"
        :nick="user.phone"
        :address="user.address"
        :reviewcnt="user.reviewcnt"
        @openAddModal="openAddModal"
      />
    </div>
    <user-add-modal v-if="addModal" :person="userList[selRow]" @close="close" />
  </div>
</template>

<script>
import row from "./userRow";
import userAddModal from "./AdminUserAdd";
import axios from "axios";
export default {
  mounted() {
    var userAddBtn = document.getElementById("userAddBtn");
    userAddBtn.addEventListener("click", () => {
      // this.addModal = 1;
      axios
        .get("http://127.0.0.1:8000/market/qrcode_page/0/0/")
        .then(response => {
          console.log(response.data);
          this.userList = response.data;
        });
    });
  },
  methods: {
    openAddModal(index) {
      this.addModal = 1;
      this.selRow = index;
      console.log(index);
    },
    close() {
      this.addModal = 0;
      this.selRow = -1;
    }
  },
  name: "AdminUser",
  components: { row, userAddModal },
  data() {
    return {
      addModal: 0,
      selRow: -1,
      id: "ID",
      nick: "닉네임",
      address: "주소",
      reviewcnt: "리뷰 수",
      userList: [
        {
          id: "이설유",
          nick: "soulyu",
          address: "부천",
          reviewcnt: "4"
        },
        {
          id: "김윤재",
          nick: "yoonjae",
          address: "봉천",
          reviewcnt: "3"
        },
        {
          id: "박권응",
          nick: "kwoneyng",
          address: "신림",
          reviewcnt: "4"
        },
        {
          id: "백민주",
          nick: "minzu",
          address: "일산",
          reviewcnt: "1"
        },
        {
          id: "윤가영",
          nick: "gayoung",
          address: "서울대입구",
          reviewcnt: "2"
        }
      ]
    };
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
* {
  font-family: "Jua", sans-serif;
  box-sizing: border-box;
}
.adminUserWrap {
  position: relative;
  margin: 3rem 3rem;
  background-color: rgba(252, 252, 252, 0.589);
  border-radius: 15px;
  overflow: auto;
}
#colId {
  position: absolute;
  top: 15%;
  width: 200px;
  left: 15%;
  font-size: 40px;
}
#userData {
  margin-bottom: 15px;
  text-align: center;
}
#userAddBtn {
  position: absolute;
  width: 180px;
  height: 60px;
  font-size: 30px;
  background-color: rgb(255, 200, 200);
  border-radius: 30px;
  border: solid 1px white;
  right: 5%;
  top: 5%;
  cursor: pointer;
  outline: 0;
}
#userList {
  position: absolute;
  top: 20%;
  width: 100%;
}
</style>