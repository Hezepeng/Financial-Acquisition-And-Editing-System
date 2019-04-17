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
            <basic-form table-name="performance_commitment_arrangement" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排" :company-package-id="item.row_id"></basic-form>
            <basic-form table-name="performance_commitment_arrangement_commitment_period" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺期间" :company-package-id="item.row_id"></basic-form>
            <basic-form table-name="performance_commitment_arrangement_committed_performance" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩" :company-package-id="item.row_id"></basic-form>
            <basic-table table-name="arrangement_committed_performance_commitment_to_net_profit" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩-承诺净利润" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="committed_performance_commitment_to_net_operating_cash_flow" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩-承诺经营性现金流量净额" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="committed_performance_commitment_to_sign_contract_amount" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩-承诺签订合同金额" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="arrangement_committed_performance_committed_inventory" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩-承诺存货" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="committed_performance_committed_inventory_recovery_rate" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩-承诺存货-回收率" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="committed_performance_committed_inventory_turnover_rate" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩-承诺存货-周转率" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="committed_performance_commitment_to_accounts_receivable" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩-承诺应收账款" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="performance_commitment_to_accounts_receivable_recovery_rate" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩-承诺应收账款-回收率" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="performance_commitment_to_accounts_receivable_turnover_rate" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩-承诺应收账款-周转率" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="committed_performance_commitment_to_long_term_receivables" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩-承诺长期应收款" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="performance_commitment_to_long_term_receivables_recovery_rate" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩-承诺长期应收款-回收率" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="performance_commitment_to_long_term_receivables_turnover_rate" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩-承诺长期应收款-周转率" :company-package-id="item.row_id"></basic-table>
            <basic-form table-name="arrangement_commitment_performance_computing_criteria" :pdf-id="pdfId" title="业绩承诺和补偿-业绩承诺安排-承诺业绩计算标准" :company-package-id="item.row_id"></basic-form>
            <basic-form table-name="performance_forecast_compensation" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿" :company-package-id="item.row_id"></basic-form>
            <basic-table table-name="performance_forecast_compensation_compensation_period" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿期间" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="performance_forecast_compensation_compensation_amount" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿金额" :company-package-id="item.row_id"></basic-table>
            <basic-form table-name="commitment_net_profit_operational_cash_flow_contract_amount" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿方式-承诺净利润/经营性现金流量金额/签订合同金额" :company-package-id="item.row_id"></basic-form>
            <basic-form table-name="operational_cash_flow_contract_amount_share_compensation" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿方式-承诺净利润/经营性现金流量金额/签订合同金额-股份补偿" :company-package-id="item.row_id"></basic-form>
            <basic-form table-name="profit_operational_cash_flow_contract_amount_cash_compensation" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿方式-承诺净利润/经营性现金流量金额/签订合同金额-现金补偿" :company-package-id="item.row_id"></basic-form>
            <basic-form table-name="forecast_compensation_compensation_mode_committed_inventory" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿方式-承诺存货" :company-package-id="item.row_id"></basic-form>
            <basic-form table-name="forecast_compensation_compensation_mode_accounts_receivable" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿方式-应收账款" :company-package-id="item.row_id"></basic-form>
            <basic-form table-name="forecast_compensation_compensation_mode_long_term_receivables" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿方式-长期应收款" :company-package-id="item.row_id"></basic-form>
            <basic-table table-name="performance_forecast_compensation_compensation_implementation" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿实施" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="to_net_profit_contract_amount_amount_share_compensation" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿实施-承诺净利润经营性现金流量金额/签订合同金额-股份补偿" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="to_net_profit_contract_amount_amount_cash_compensation" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿实施-承诺净利润经营性现金流量金额/签订合同金额-现金补偿" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="implementation_committed_inventory_cash_compensation" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿实施-承诺存货-现金补偿" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="implementation_accounts_receivable_cash_compensation" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿实施-应收账款-现金补偿" :company-package-id="item.row_id"></basic-table>
            <basic-table table-name="implementation_long_term_receivables_cash_compensation" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿-补偿实施-长期应收款-现金补偿" :company-package-id="item.row_id"></basic-table>
            <basic-form table-name="performance_forecast_compensation_guarantee" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测补偿担保" :company-package-id="item.row_id"></basic-form>
            <basic-form table-name="forecast_guarantee_guarantee_mode_share_pledge_guarantee" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测担保-担保方式-股份质押担保" :company-package-id="item.row_id"></basic-form>
            <basic-form table-name="performance_forecast_guarantee_guarantee_mode_margin_guarantee" :pdf-id="pdfId" title="业绩承诺和补偿-业绩预测担保-担保方式-保证金担保" :company-package-id="item.row_id"></basic-form>
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
    name: 'PerformanceCommitmentCompensation',
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

