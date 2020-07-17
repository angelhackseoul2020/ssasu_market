<template>
  <div class="adminUserWrap">
    <div class="adminUser">유저리스트</div>
    <button id="userAddBtn">유저 추가</button>
    <div id="colId">
      <p id="colHead">ID</p>
      <p id="userData" v-for="user in userList" :key="user">{{user.name}}</p>
    </div>
    <div id="colNick">
      <p id="colHead">닉네임</p>
      <p id="userData" v-for="user in userList" :key="user">{{user.nick}}</p>
    </div>
    <div id="colAddress">
      <p id="colHead">주소</p>
      <p id="userData" v-for="user in userList" :key="user">{{user.address}}</p>
    </div>
    <div id="colReview">
      <p id="colHead">리뷰</p>
      <p id="userData" v-for="user in userList" :key="user">{{user.review}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminUser",
  components: {},
  data(){
    return{
      userList:[
        {
          'name':'이설유',
          'nick':'soulyu',
          'address':'부천',
          'review':4
        },
        {
          'name':'김윤재',
          'nick':'yoonjae',
          'address':'봉천',
          'review':3        
        },
        {
          'name':'박권응',
          'nick':'kwoneyng',
          'address':'신림',
          'review':4        
        },
        {
          'name':'백민주',
          'nick':'minzu',
          'address':'일산',
          'review':1        
        },
        {
          'name':'윤가영',
          'nick':'gayoung',
          'address':'서울대입구',
          'review':2        
        },
      ]
    }
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
#colId{
  position: absolute;
  top: 15%;
  width: 200px;
  left: 15%;
  font-size: 40px;
}
#colNick{
  position:absolute;
  width: 200px;
  top: 15%;
  left: 35%;
  font-size: 40px;
}
#colAddress{
  position: absolute;
  width: 200px;
  top: 15%;
  left: 55%;
  font-size: 40px;
}
#colReview{
  position: absolute;
  width: 200px;
  top: 15%;
  left: 75%;
  font-size: 40px;
}
#colHead{
  font-size: 50px;
  margin-bottom: 20px;
  text-align: center;
}
#userData{
  margin-bottom: 15px;
  text-align: center;
}
#userAddBtn{
  position:absolute;
  width: 180px;
  height: 60px;
  font-size: 30px;
  background-color: rgb(255,200,200);
  border-radius: 30px;
  border: solid 1px white;
  right:5%;
  top:5%
}
</style>