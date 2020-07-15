<template>
    <div>
        <img id='intro' src="../assets/bgimg.png" alt="">
        <img id='charactor' src="../assets/logo2.png" alt="">
        <div id="intro-text">"나의 전통시장 찾기"</div>
        <div id="intro-sub">"소상공인이 살아야 지역경제가 산다"</div>
        <div id="login-btn">로그인</div>
        <div id="signup-btn">회원가입</div>
        <login-modal v-if="openLoginModal"
            :width="width"
            :height="height"
            @loginSub="loginSub"
            @closeLoginModal="closeLoginModal"
        />
        <signup-modal v-if="openSignupModal"
            :width="width"
            :height="height"
            @signSub="signSub"
            @closeSignModal="closeSignModal"
        />
    </div>
</template>

<script>
import LoginModal from './LoginModal'
import SignupModal from './SignupModal'

export default {
    components:{
        LoginModal, SignupModal
    },
    props:{
        width:{
            type:Number
        },
        height:{
            type:Number
        }
    },
    data(){
        return{
            openLoginModal:0,
            openSignupModal:0,
        }
    },
    mounted(){
        this.arrange()
        this.addfuction()
        },
    methods:{
        arrange(){
            var intro = document.getElementById('intro')
            intro.style.width = this.width + 'px'
            intro.style.height = this.height + 'px'
            intro.addEventListener('click',()=>{
                this.$emit('close')
            })
            var charactor = document.getElementById('charactor')
            charactor.style.width = '360px'
            charactor.style.height = '400px'
            charactor.style.position = 'absolute'
            charactor.style.top = (this.height/2 - 300) +'px'
            charactor.style.left = (this.width/2 - 180) + 'px'
            var introText = document.getElementById('intro-text')
            introText.style.top = (this.height/2 + 120) +'px'
        },
        addfuction(){
            var lgbtn = document.getElementById('login-btn')
            var subtn = document.getElementById('signup-btn')
            lgbtn.addEventListener('click',()=>{
                console.log('click login btn');
                this.openLoginModal = 1
            })
            subtn.addEventListener('click',()=>{
                console.log('click sign up btn');
                this.openSignupModal = 1
            })
        },
        loginSub(){
            this.openLoginModal = 0
            this.$emit('login')
        },
        closeLoginModal(){
            this.openLoginModal = 0
        },
        signSub(){
            this.openSignupModal = 0
        },
        closeSignModal(){
            this.openSignupModal = 0
        }


    }
}
</script>

<style>
#charactor{
    position:absolute;
}
#intro-text{
    position: absolute;
    width:100%;
    left:0;
    text-align: center;
    font-size: 60px;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
#intro-sub{
    position: absolute;
    width:100%;
    left:0;
    text-align: center;
    font-size: 28px;
    color: #aaaaaa;
    bottom: 90px;
}
#login-btn{
    position: absolute;
    right: 220px;
    top: 30px;
    border-radius: 45px;
    text-align: center;
    padding:10px 35px;
    font-size: 30px;
    background-color: #ffcccc;
    border: solid #ffffff 1px;
    cursor: pointer;
}
#signup-btn{
    position: absolute;
    right: 30px;
    top: 30px;
    text-align: center;
    padding: 10px 25px;
    font-size: 30px;
    background-color: #aaaaff;
    border-radius: 45px;
    border: solid #ffffff 1px;
    cursor: pointer;
}

</style>