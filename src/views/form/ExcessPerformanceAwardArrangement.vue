<template>
  <div>
    <el-row id="area" :gutter="10" style="margin:30px 10px 10px 15px;">
      <el-col :span="11">
        <el-card :body-style="{ padding: '5px' }">
          <div style="padding: 5px">
            当前编辑的文件名：
            <span style="color: #409EFF">
            {{this.editPdfName}}
            </span>
          </div>
        </el-card>
        <div style="height: 10px"></div>
        <el-card :body-style="{ padding: '0px' }">
          <div v-show="showPdf">
            <div ref="pdfviewer" class="pdfobject-container"></div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="13" style="height:800px;overflow-y: scroll;" v-if="pdfId">
        <el-tabs type="border-card" v-if="showTabs">
          <el-tab-pane :label="item.package_name" v-for="(item,index) in packageList">
            <el-row>
              <el-col>
                <el-button type="danger" @click="onDeleteCompanyPackage(item.row_id)" style="margin-bottom: 10px;float: right">删除该套件</el-button>
              </el-col>
            </el-row>
            <basic-table table-name="reward_period" :pdf-id="pdfId" title="超额业绩奖励安排-奖励期间" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="trigger_condition" :pdf-id="pdfId" title="超额业绩奖励安排-触发条件" :company-package-id="item.row_id"></basic-table>
            <basic-form table-name="assessment_index" :pdf-id="pdfId" title="超额业绩奖励安排-考核指标" :company-package-id="item.row_id"></basic-form>
            <basic-form table-name="reward_amount" :pdf-id="pdfId" title="超额业绩奖励安排-奖励金额" :company-package-id="item.row_id"></basic-form>
            <basic-form table-name="payment_arrangements" :pdf-id="pdfId" title="超额业绩奖励安排-支付安排" :company-package-id="item.row_id"></basic-form>
            <basic-table table-name="accounting_treatment" :pdf-id="pdfId" title="超额业绩奖励安排-账务处理" :company-package-id="item.row_id"></basic-table>
          </el-tab-pane>
          <el-tab-pane label="新增套件">
            <basic-new-target-package :pdf-id="pdfId" :module-name="this.$options.name" :company-package-list="packageList" @sendNewTargetPackage="onNewTargetPackage"></basic-new-target-package>
          </el-tab-pane>
        </el-tabs>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import BasicForm from '../../components/Form/BasicForm'
  import BasicTable from '../../components/Form/BasicTable'
  import PDFObject from 'pdfobject'
  import { deleteCompanyPackage, getAllCompanyPackage } from '../../api/form'
  import BasicNewTargetPackage from '../../components/Form/BasicNewTargetPackage'

  export default {
    name: 'ExcessPerformanceAwardArrangement',
    components: { BasicNewTargetPackage, BasicTable, BasicForm },

    data() {
      return {
        screenHeight: document.documentElement.clientHeight,
        showPdf: true,
        showTabs: true,
        packageList: []
      }
    },
    computed: {
      pdfId: function() {
        return this.$store.state.app.editPdfId
      },
      editPdfName: function() {
        return this.$store.state.app.editPdfName
      },
      documentOriginLocation: function() {
        return '/src/pdf/' + this.$store.state.app.editPdfName
      }

    },
    mounted() {
      if (!this.pdfId) {
        this.$alert('请先选择要编辑的文件', '温馨提示', {
          confirmButtonText: '去选择文件',
          center: true,
          callback: action => {
            this.$router.push({ name: 'pdfList' })
          }
        })
      } else {
        this.initPackageList()
      }
    },
    watch: {
      toPage: {
        handler: function(val, oldVal) {
          this.$nextTick(function() {
            const pdfnode = this.$refs.pdfviewer
            // const pdfnodeleft = this.$refs.pdfviewerleft
            PDFObject.embed(this.documentOriginLocation, pdfnode, val)
            // PDFObject.embed(this.documentOriginLocation, pdfnodeleft, val)
          })
        },
        deep: true,
        immediate: true
      }
    },
    methods: {
      reloadPanel() {
        let _this = this
        this.initPackageList().then(function() {
          _this.showTabs = false
          _this.$nextTick(() => {
            _this.showTabs = true
          })
        })
      },
      onNewTargetPackage() {
        this.$message({
          message: '生成表格成功',
          type: 'success'
        })
        this.reloadPanel()
      },
      onDeleteCompanyPackage(row_id) {
        let _this = this
        this.$confirm('此操作将永久删除本标的公司组合下的【资产评估】【业绩承诺和补偿】【业绩承诺完成情况】【减值测试安排】【超额业绩奖励安排】的所有录入数据, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          deleteCompanyPackage(row_id).then(response => {
            let res = response.data
            if (res.code === 1) {
              this.$message({
                message: '删除成功',
                type: 'success'
              })
              _this.reloadPanel()
            }
          }).catch(exception => {
            console.log(exception)
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })

      },
      initPackageList() {
        return new Promise((resolve, reject) => {
          getAllCompanyPackage(this.pdfId, this.$options.name).then(response => {
            let res = response.data
            this.packageList = res.data
            resolve('success')
          }).catch(exception => {
            console.log(exception)
            reject('fail')
          })
        })
      }
    }

  }
</script>

<style scoped>
  .pdfobject-container {
    height: 800px;
    width: 100%;
    display: block;
    margin: auto;
  }

  .pdfobject {
    border: 1px solid #666;
  }
</style>

