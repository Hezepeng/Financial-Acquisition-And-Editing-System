import Vue from 'vue'
import Router from 'vue-router'

// in development-env not use lazy-loading, because lazy-loading too many pages will cause webpack hot update too slow. so only in production use lazy-loading;
// detail: https://panjiachen.github.io/vue-element-admin-site/#/lazy-loading

Vue.use(Router)

/* Layout */
import Layout from '../views/layout/Layout'

/**
 * hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
 *                                if not set alwaysShow, only more than one route under the children
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noredirect           if `redirect:noredirect` will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar
    breadcrumb: false            if false, the item will hidden in breadcrumb(default is true)
  }
 **/
export const constantRouterMap = [
  { path: '/login', component: () => import('@/views/login/index'), hidden: true },
  { path: '/404', component: () => import('@/views/404'), hidden: true },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    name: 'Dashboard',
    hidden: true,
    children: [{
      path: 'dashboard',
      component: () => import('@/views/dashboard/index')
    }]
  },
  {
    path: '/pdf',
    component: Layout,
    meta: { title: 'PDF文件管理', icon: 'example' },
    children: [{
      path: '/pdf/list',
      name: 'pdfList',
      component: () => import('@/views/form/PdfTable'),
      meta: { title: 'PDF列表', icon: 'form' }

    }]
  },
  {
    path: '/form',
    component: Layout,
    meta: { title: '录入表单', icon: 'example' },
    children: [
      {
        path: 'basicPlan',
        name: 'basicPlan',
        component: () => import('@/views/form/BasicPlan'),
        meta: { title: '基本方案', icon: 'form' }
      },
      {
        path: 'cashSharePurchaseAsset',
        name: 'cashSharePurchaseAsset',
        component: () => import('@/views/form/CashSharePurchaseAsset'),
        meta: { title: '现金股份购买资产', icon: 'form' }
      },
      {
        path: 'raiseMatchFund',
        name: 'raiseMatchFund',
        component: () => import('@/views/form/RaiseMatchFund'),
        meta: { title: '募集配套资金', icon: 'form' }
      },
      {
        path: 'assetValuation',
        name: 'assetValuation',
        component: () => import('@/views/form/AssetValuation'),
        meta: { title: '资产评估', icon: 'form' }
      },
      {
        path: 'performanceCommitmentCompensation',
        name: 'performanceCommitmentCompensation',
        component: () => import('@/views/form/PerformanceCommitmentCompensation'),
        meta: { title: '业绩承诺和补偿', icon: 'form' }
      },
      {
        path: 'performanceCommitmentCompletion',
        name: 'performanceCommitmentCompletion',
        component: () => import('@/views/form/PerformanceCommitmentCompletion'),
        meta: { title: '业绩承诺完成情况', icon: 'form' }
      },
      {
        path: 'impairmentTestArrangement',
        name: 'impairmentTestArrangement',
        component: () => import('@/views/form/ImpairmentTestArrangement'),
        meta: { title: '减值测试安排', icon: 'form' }
      },
      {
        path: 'excessPerformanceAwardArrangement',
        name: 'excessPerformanceAwardArrangement',
        component: () => import('@/views/form/ExcessPerformanceAwardArrangement'),
        meta: { title: '超额业绩奖励安排', icon: 'form' }
      }

    ]
  },
  // {
  //   path: '/example',
  //   component: Layout,
  //   redirect: '/example/table',
  //   name: 'Example',
  //   meta: { title: 'Example', icon: 'example' },
  //   children: [
  //     {
  //       path: 'table',
  //       name: 'Table',
  //       component: () => import('@/views/table/index'),
  //       meta: { title: 'Table', icon: 'table' }
  //     },
  //     {
  //       path: 'tree',
  //       name: 'Tree',
  //       component: () => import('@/views/tree/index'),
  //       meta: { title: 'Tree', icon: 'tree' }
  //     }
  //   ]
  // },

  // {
  //   path: '/form',
  //   component: Layout,
  //   children: [
  //     {
  //       path: 'index',
  //       name: 'Form',
  //       component: () => import('@/views/form/index'),
  //       meta: { title: 'Form', icon: 'form' }
  //     }
  //   ]
  // },
  //
  // {
  //   path: '/nested',
  //   component: Layout,
  //   redirect: '/nested/menu1',
  //   name: 'Nested',
  //   meta: {
  //     title: 'Nested',
  //     icon: 'nested'
  //   },
  //   children: [
  //     {
  //       path: 'menu1',
  //       component: () => import('@/views/nested/menu1/index'), // Parent router-view
  //       name: 'Menu1',
  //       meta: { title: 'Menu1' },
  //       children: [
  //         {
  //           path: 'menu1-1',
  //           component: () => import('@/views/nested/menu1/menu1-1'),
  //           name: 'Menu1-1',
  //           meta: { title: 'Menu1-1' }
  //         },
  //         {
  //           path: 'menu1-2',
  //           component: () => import('@/views/nested/menu1/menu1-2'),
  //           name: 'Menu1-2',
  //           meta: { title: 'Menu1-2' },
  //           children: [
  //             {
  //               path: 'menu1-2-1',
  //               component: () => import('@/views/nested/menu1/menu1-2/menu1-2-1'),
  //               name: 'Menu1-2-1',
  //               meta: { title: 'Menu1-2-1' }
  //             },
  //             {
  //               path: 'menu1-2-2',
  //               component: () => import('@/views/nested/menu1/menu1-2/menu1-2-2'),
  //               name: 'Menu1-2-2',
  //               meta: { title: 'Menu1-2-2' }
  //             }
  //           ]
  //         },
  //         {
  //           path: 'menu1-3',
  //           component: () => import('@/views/nested/menu1/menu1-3'),
  //           name: 'Menu1-3',
  //           meta: { title: 'Menu1-3' }
  //         }
  //       ]
  //     },
  //     {
  //       path: 'menu2',
  //       component: () => import('@/views/nested/menu2/index'),
  //       meta: { title: 'menu2' }
  //     }
  //   ]
  // },
  //
  // {
  //   path: 'external-link',
  //   component: Layout,
  //   children: [
  //     {
  //       path: 'https://panjiachen.github.io/vue-element-admin-site/#/',
  //       meta: { title: 'External Link', icon: 'link' }
  //     }
  //   ]
  // },

  { path: '*', redirect: '/404', hidden: true }
]

export default new Router({
  // mode: 'history', //后端支持可开
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})