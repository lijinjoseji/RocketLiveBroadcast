<template>
    <div>
        <div class="whole-div" v-bind:class="{ blur: $store.state.background_blur }">
            <el-button type="text" id="open-room-btn" v-if="$store.state.isTeacher && $route.path === '/roomList'"
                       @click="openCreateRoomDialog">创建房间
            </el-button>
            <el-button class="home-btn" type="text" @click="showRoomList">主页</el-button>
            <div id="blank"></div>
            <div id="right-btns">
                <el-button class="right-text-btn" type="text"
                           @click="logout" v-if="logged">Log Out
                </el-button>
                <el-button class="right-text-btn" type="text"
                           @click="showInfoDialog" v-if="logged">{{userName}}
                </el-button>
                <el-button class="right-text-btn" type="text"
                           @click="openRegisterDialog" v-if="!logged">Register
                </el-button>
                <el-button class="right-text-btn" type="text"
                           @click="openLoginDialog" v-if="!logged">Log in
                </el-button>
            </div>
        </div>
        <register-modal-dialog></register-modal-dialog>
        <login-modal-dialog></login-modal-dialog>
        <info-modal-dialog></info-modal-dialog>
        <forget-modal-dialog></forget-modal-dialog>
        <create-room-modal-dialog></create-room-modal-dialog>
    </div>
</template>

<script>
import RegisterModalDialog from './RegisterModalDialog.vue'
import LoginModalDialog from './LoginModalDialog'
import InfoModalDialog from './InfoModalDialog'
import ForgetModalDialog from './ForgetModalDialog'
import CreateRoomModalDialog from './CreateRoomModalDialog'

export default {
    components: {
        RegisterModalDialog,
        LoginModalDialog,
        InfoModalDialog,
        ForgetModalDialog,
        CreateRoomModalDialog
    },
    data: function () {
        return {
            isTeacher: false,
            isBlur: true
        }
    },
    computed: {
        userName: function () {
            return this.$store.state.nickname
        },
        logged: function () {
            return this.$store.state.account !== null
        }
    },
    methods: {
        switchBlur: function () {
            this.isBlur = !this.isBlur
        },
        showRegister: function () {
            this.$emit('goto', 'Register')
        },
        logout: function () {
            this.loged = false
            this.$store.dispatch('logout')
        },
        showLogin: function () {
            this.$emit('goto', 'LoginPage')
        },
        showInfoDialog: function () {
            this.$store.dispatch('openInfoDialog')
        },
        showCreateRoom: function () {
            // this.$emit('goto', 'CreateRoom')
            this.$router.push('createRoom')
        },
        showRoomList: function () {
            this.$store.dispatch('getRooms')
            this.$store.dispatch('getHistory')
            this.$router.push('/roomList')
        },
        openRegisterDialog: function () {
            this.$store.dispatch('openRegisterDialog')
        },
        openLoginDialog: function () {
            this.$store.dispatch('openLoginDialog')
        },
        openCreateRoomDialog: function () {
            this.$store.dispatch('openCreateRoomDialog')
        }
    }
}
</script>

<style scoped>
.whole-div {
    display: flex;
    align-items: center;
    border: none;
    position: fixed;
    background: linear-gradient(to bottom, #F4F7F6 , #E3E3E3);
    width: 100%;
    z-index: 100;
}

.home-btn {
    color: black;
    font-weight: bold;
}

.right-text-btn {
    font-size: 16px;
    color: black;
    font-weight: bold;
    margin-left: 0;
}

button {
    margin: 8px;
    width: 80px;
}

#blank {
    flex-grow: 1;
}

#open-room-btn {
    background-color: #a5d9dd;
    color: white;
    margin-left: 20px;
    min-width: 80px;
}
</style>

