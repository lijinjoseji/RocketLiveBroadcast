<template>
    <div>
        <transition name="modal">
            <div class="modal-mask" v-if="this.$store.state.showForget">
                <div class="modal-wrapper">
                    <div class="container">
                        <img class="side-img" src="../assets/forget-password-image.svg">
                        <div class="right-side">
                            <div class="header">
                                <p class="title">Find Password</p>
                                <el-button type="text" class="close-btn"
                                           @click="closeForget">×
                                </el-button>
                            </div>
                            <div class="dialog-body" @keyup.enter="changePassword">
                                <input type="text" placeholder="E-MAIL OR PHONE NUMBER" v-model="account">
                                <div class="vertificate">
                                    <input type="text" placeholder="VERIFICATION CODE" class="vertificate-input input"
                                           v-model="vertificateCode">
                                    <el-button type="text" class="send-code-btn" @click="sendVertificateCode">send
                                    </el-button>
                                </div>
                                <input type="password" class="input password" placeholder="PASSWORD" v-model="password">
                                <input type="password" class="input sure-password" placeholder="COMFIRM PASSWORD"
                                       v-model="confirmPassword">
                                <el-button @click="changePassword" class="sure-btn shadow-m">RESET PASSWORD</el-button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
import LoginModalDialog from './LoginModalDialog'

export default {
    components: {
        LoginModalDialog,
    },
    data: function () {
        return {
            account: '',
            password: '',
            confirmPassword: '',
            vertificateCode: '',
        }
    },
    methods: {
        closeForget: function () {
            this.$store.dispatch('closeForgetDialog')
        },
        showErrorMes: function (mes) {
            this.$message({
                message: mes,
                type: 'warning'
            })
        },
        isPassword () {
            let patrn = /^(\w){8,20}$/
            return patrn.test(this.password)
        },
        isRightPhoneNum () {
            let phone = this.account
            return /^1[3|4|5|7|8]\d{9}$/.test(phone)
        },
        isRightEmail () {
            let re = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/
            return re.test(this.account)
        },
        changePassword: function () {
            if (this.account === '') {
                this.showErrorMes('请填写电子邮箱或手机号码')
                return
            }
            if (!(this.isRightEmail() || this.isRightPhoneNum())) {
                this.showErrorMes('不是有效的电子邮箱或手机号码')
                return
            }
            // todo: make sure password's format
            if (this.password !== this.confirmPassword) {
                this.showErrorMes('两次密码不一致')
                return
            }
            if (!this.isPassword()) {
                this.showErrorMes('密码格式不正确，请使用8至16位的数字、字母和下划线组合')
                return
            }
            if (this.vertificateCode === '') {
                this.showErrorMes('请填写验证码')
                return
            }
            this.$store.dispatch('forgetPassword', {
                account: this.account,
                password: new window.Hashes.SHA256().hex(this.password),
                vertificateCode: this.vertificateCode
            })
        },
        sendVertificateCode () {
            if (this.account === '') {
                window.alert('请输入用户名')
                return
            }
            if (this.isRightPhoneNum()) {
                this.$store.dispatch('sendVertificateCode', {
                    account: this.account,
                    mode: 'forget',
                    type: 'phone'
                })
            } else if (this.isRightEmail()) {
                this.$store.dispatch('sendVertificateCode', {
                    account: this.account,
                    mode: 'forget',
                    type: 'email'
                })
            } else {
                this.showErrorMes('不是有效的电子邮箱或手机号码')
            }
        },
    }
}
</script>

<style scoped>
.container {
    width: 480px;
    height: 460px;
    margin: 0 auto;
    background-color: #fff;
    border-radius: 20px;
    box-shadow: 0 12px 25px -6px rgba(0, 0, 0, .35);
    transition: all .3s ease;
    display: flex;
}

.side-img {
    height: 460px;
    margin-right: auto;
    margin-left: 0;
}

.right-side {
    margin-top: 15px;
    position: relative;
    left: -37px;
}

.header {
    margin-left: -60px;
    color: #42b983;
    display: flex;
    justify-content: space-around;
}

.title {
    font-size: 18px;
    text-align: left;
    color: #808080;
}

.close-btn {
    color: #cacaca;
    font-size: 30px;
    position: relative;
    left: 100px;
    top: -13px;
}

.dialog-body {
    display: flex;
    flex-direction: column;
    margin-top: 60px;
    margin-left: -6px;
}

input {
    border-left: none;
    border-right: none;
    border-top: none;
    outline: none;
    font-size: 13px;
    margin-bottom: 20px;
    padding-bottom: 8px;
    padding-left: 0.2em;
}

.sure-btn {
    color: white;
    font-size: 17px;
    background-color: #269a77;
    border-radius: 20px;
    margin-top: 15px;
    padding: 12px;
}

.vertificate {
    display: flex;
    justify-content: space-around;
}

.vertificate-input {
}

.send-code-btn {
    font-size: 18px;
    font-weight: bold;
    margin-top: -24px;
    margin-left: 15px;
    float: right;
}

</style>
