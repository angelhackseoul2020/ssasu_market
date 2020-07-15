<template>
  <div>
    <div id="sign-modal-back" :style="{width:width+'px', height:height+'px'}">
    </div>
    <div id="sign-modal">
        <div id="sign-id-text">아이디</div>
        <input id="sign-id-input" type="text" placeholder="아이디">
        <div id="sign-nick-text">닉네임</div>
        <input type="text" id="sign-nick-input" placeholder="닉네임">
        <div id="sign-pw-text">비밀번호</div>
        <div id="sign-email-text">이메일</div>
        <input type="email" id="sign-email-input" placeholder="이메일">
        <div id="sign-phone-text">연락처</div>
        <input type="text" id="sign-phone-input" placeholder="연락처">
        <input id="sign-pw-input" type="password" placeholder="비밀번호">
        <div id="sign-submit">로그인</div>
    </div>
  </div>
</template>

<script>
export default {
    props:{
        width:{
            type:Number
        },
        height:{
            type:Number
        }
    },
    data(){
        return {
        }
    },
    mounted(){
        var signModal = document.getElementById('sign-modal')
        signModal.style.top = this.height/2 - 350 + 'px'
        signModal.style.left = this.width/2 - 500 + 'px'
        var submit = document.getElementById('sign-submit')
        submit.addEventListener('click',()=>{
          this.$emit('signSub')
        })
        var signBack = document.getElementById('sign-modal-back')
        signBack.addEventListener('click',()=>{
          this.$emit('closeSignModal')
        })
    }
}
</script>

<style>
#sign-modal-back{
  position: absolute;
  opacity: 0.96;
  top:0;
  left: 0;
}
#sign-modal{
    position:absolute;
    width: 1000px;
    height: 700px;
    background-color: white;
    border-radius: 30px;
}
#sign-id-text{
    position: absolute;
    width: 250px;
    height: 70px;
    font-size: 50px;
    padding: 10px 0;
    text-align: end;
    top:50px;
    left:100px;
}
#sign-pw-text{
    position: absolute;
    width: 250px;
    height: 70px;
    font-size: 50px;
    padding: 10px 0;
    text-align: end;
    top:150px;
    left:100px;
}
#sign-nick-text{
  position: absolute;
  width: 250px;
  height: 70px;
  font-size: 50px;
  text-align: end;
  top: 260px;
  left: 100px;
}
#sign-email-text{
  position: absolute;
  width: 250px;
  height: 70px;
  font-size: 50px;
  text-align: end;
  top: 360px;
  left: 100px;
}
#sign-phone-text{
  position: absolute;
  width: 250px;
  height: 70px;
  font-size: 50px;
  text-align: end;
  top: 460px;
  left: 100px;
}
#sign-id-input{
    position:absolute;
    width: 330px;
    height: 70px;
    border:none;
    font-size: 50px;
    background: #ddddff;
    border-radius: 25px;
    padding-left: 25px;
    top: 60px;
    left: 400px;
}
#sign-pw-input{
    position:absolute;
    width: 330px;
    height: 70px;
    border:none;
    font-size: 50px;
    background: #ddddff;
    border-radius: 25px;
    padding-left: 25px;
    top: 160px;
    left: 400px;
}
#sign-nick-input{
  position: absolute;
  width:330px;
  height: 70px;
  border: none;
  font-size: 50px;
  background-color: #ddddff;
  border-radius: 25px;
  padding-left: 25px;
  top: 260px;
  left:400px;
}
#sign-email-input{
  position: absolute;
  width: 330px;
  height: 70px;
  border:none;
  font-size: 50px;
  background-color: #ddddff;
  border-radius: 25px;
  padding-left: 25px;
  top: 360px;
  left: 400px;
}
#sign-phone-input{
  position: absolute;
  width: 330px;
  height: 70px;
  border:none;
  font-size: 50px;
  background-color: #ddddff;
  border-radius: 25px;
  padding-left: 25px;
  top: 460px;
  left: 400px;
}

#sign-submit{
    position:absolute;
    width: 160px;
    height: 50px;
    font-size: 30px;
    text-align: center;
    padding-top: 8px;
    background-color: #ddddff;
    border-radius: 40px;
    left: 420px;
    top:600px;
    cursor: pointer;
}

</style>