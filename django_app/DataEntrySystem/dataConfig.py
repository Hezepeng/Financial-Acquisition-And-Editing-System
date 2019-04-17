# pdf文件列表
pdf_information_key_value_list = {
  'pdf_id': 'ID',
  'full_name': '文件名',
  'simple_name': '文件简称',
  'create_time': '创建时间'
}

pdf_information_key_type_list = {
  'pdf_id': 'text',
  'full_name': 'text',
  'simple_name': 'text',
  'create_time': 'datetime'
}


# 基本方案-基本信息-table
basic_plan_essential_information_key_value_list = {
  "listed_companies_abbreviation": "上市公司简称",
  "listing_place": "上市地点",
  "listed_companies_securities_code": "上市公司证券代码",
  "listed_companies": "上市公司所属行业",
  "listed_companies_main_business": "上市公司主营业务",
  "target_company": "标的公司",
  "transacted_assets_to_target_company_stock_ratio": "交易资产所占标的公司的股权比例（%）",
  "target_company_inc": "标的公司所属行业",
  "target_company_main_business": "标的公司主营业务",
}

basic_plan_essential_information_key_type_list = {
  "listed_companies_abbreviation": "text",
  "listing_place": "text",
  "listed_companies_securities_code": "text",
  "listed_companies": "text",
  "listed_companies_main_business": "textarea",
  "target_company": "textarea",
  "transacted_assets_to_target_company_stock_ratio": "ratio",
  "target_company_inc": "textarea",
  "target_company_main_business": "textarea"
}

# 基本方案-交易类型-form
basic_plan_transaction_type_key_value_list = {
  "constituting_major_asset_restructuring_flag": "是否构成重大资产重组",
  "for_affiliated_transactions_flag": "是否为关联交易",
  "listed_companies_enough_to_change_control_rights_flag": "是否够成上市公司控制权变化",
  "asset_replacement_flag": "资产置换",
  "cash_purchase_assets_flag": "现金购买资产",
  "issuing_share_to_purchase_assets_flag": "发行股份购买资产",
  "assets_sale_flag": "出售资产",
  "absorption_merger_flag": "吸收合并",
  "discrete_flag": "分立",
  "listed_companies_acquisition_flag": "上市公司收购",
  "tender_offer_flag": "要约收购",
  "raising_matching_funds_flag": "是否募集配套资金",
}

basic_plan_transaction_type_key_type_list = {
  "constituting_major_asset_restructuring_flag": "checkbox",
  "for_affiliated_transactions_flag": "checkbox",
  "listed_companies_enough_to_change_control_rights_flag": "checkbox",
  "asset_replacement_flag": "checkbox",
  "cash_purchase_assets_flag": "checkbox",
  "issuing_share_to_purchase_assets_flag": "checkbox",
  "assets_sale_flag": "checkbox",
  "absorption_merger_flag": "checkbox",
  "discrete_flag": "checkbox",
  "listed_companies_acquisition_flag": "checkbox",
  "tender_offer_flag": "checkbox",
  "raising_matching_funds_flag": "checkbox"
}

# 基本方案-支付方式-form
basic_plan_payment_key_value_list = {
  "cash_flag": "现金",
  "cash_ratio": "现金比例",
  "share_flag": "股份",
  "share_ratio": "股份比例",
  "convertible_bonds_flag": "可转换债券",
  "convertible_bond_ratio": "可转换债券比例",
}

basic_plan_payment_key_type_list = {
  "cash_flag": "checkbox",
  "cash_ratio": "text",
  "share_flag": "checkbox",
  "share_ratio": "text",
  "convertible_bonds_flag": "checkbox",
  "convertible_bond_ratio": "text"
}

# 基本方案-标的资产交割-有限公司-table
basic_plan_assets_delivery_limited_company_key_value_list = {
  "underlying_assets_name": "标的资产名称",
  "director_supervisor_seniorstock_delivery_time": "董事、监事、高级管理人员股权交割时间",
  "shareholder_controller_stock_delivery_time": "控股股东及实际控制人股权交割时间",
  "other_shareholders_tock_delivery_times": "其他股东股权交割时间",
}

basic_plan_assets_delivery_limited_company_key_type_list = {
  "underlying_assets_name": "text",
  "director_supervisor_seniorstock_delivery_time": "text",
  "shareholder_controller_stock_delivery_time": "text",
  "other_shareholders_tock_delivery_times": "textarea"
}

# 基本方案-标的资产交割-股份有限公司-已挂牌公司-table
basic_plan_assets_delivery_limited_company_listed_companies_key_value_list = {
  "underlying_assets_name": "标的资产名称",
  "share_company_setup_time": "股份公司设立时间",
  "listing_place": "挂牌地点",
  "listing_time": "挂牌时间",
  "shareholder_limitation_arrangement": "股东限售安排",
  "listing_termination_flag": "是否终止挂牌",
  "delisting_time": "摘牌时间",
  "change_share_company_to_limited_company_time": "股份公司变更为有限公司时间",
  "shareholder_controller_stock_delivery_time": "控股股东及实际控制人股权交割时间",
  "director_supervisor_seniorstock_transfer_time": "董事、监事、高级管理人员股权过户时间",
  "other_shareholders_tock_transfer_times": "其他股东股权过户时间",
}

basic_plan_assets_delivery_limited_company_listed_companies_key_type_list = {
  "underlying_assets_name": "text",
  "share_company_setup_time": "datetime",
  "listing_place": "text",
  "listing_time": "datetime",
  "shareholder_limitation_arrangement": "textarea",
  "listing_termination_flag": "checkbox",
  "delisting_time": "text",
  "change_share_company_to_limited_company_time": "text",
  "shareholder_controller_stock_delivery_time": "text",
  "director_supervisor_seniorstock_transfer_time": "text",
  "other_shareholders_tock_transfer_times": "textarea"
}

# 基本方案-标的资产交割-股份有限公司-未挂牌公司-table
basic_plan_assets_delivery_limited_company_unlisted_companies_key_value_list = {
  "underlying_assets_name": "标的资产名称",
  "share_company_setup_time": "股份公司设立时间",
  "shareholder_limitation_arrangement": "股东限售安排",
  "change_share_company_to_limited_company_time": "股份公司变更为有限公司时间",
  "shareholder_controller_stock_delivery_time": "控股股东及实际控制人股权交割时间",
  "director_supervisor_seniorstock_transfer_time": "董事、监事、高级管理人员股权过户时间",
  "other_shareholders_tock_transfer_times": "其他股东股权过户时间",
}

basic_plan_assets_delivery_limited_company_unlisted_companies_key_type_list = {
  "underlying_assets_name": "text",
  "share_company_setup_time": "datetime",
  "shareholder_limitation_arrangement": "textarea",
  "change_share_company_to_limited_company_time": "text",
  "shareholder_controller_stock_delivery_time": "text",
  "director_supervisor_seniorstock_transfer_time": "text",
  "other_shareholders_tock_transfer_times": "textarea"
}

# 基本方案-过渡期安排-form
basic_plan_transition_arrangement_key_value_list = {
  "transition_time": "过渡期时间",
  "target_company_dividend_in_transition_flag": "过渡期内标的公司是否分红",
  "bonus_method": "分红方式",
  "transition_profit_attribution": "过渡期盈利归属",
  "transition_loss_attribution": "过渡期损失归属",
  "transition_losses_are_borne_proportionally_flag": "过渡期损失是否按比例承担",
  "transition_losses_joint_several_liability_flag": "过渡期损失是否连带承担责任",
  "transition_gains_losses_audit_time": "过渡期损益的审计时间",
  "other_transition_arrangements": "过渡期其他安排",
}

basic_plan_transition_arrangement_key_type_list = {
  "transition_time": "text",
  "target_company_dividend_in_transition_flag": "checkbox",
  "bonus_method": "textarea",
  "transition_profit_attribution": "text",
  "transition_loss_attribution": "text",
  "transition_losses_are_borne_proportionally_flag": "checkbox",
  "transition_losses_joint_several_liability_flag": "checkbox",
  "transition_gains_losses_audit_time": "text",
  "other_transition_arrangements": "textarea"
}

# 基本方案-或有负债-table
basic_plan_contingent_liability_key_value_list = {
  "debt_scope": "债务范围",
  "subject_name": "承担主体名称",
  "subject_identity": "承担主体身份",
  "prorated_commitment_flag": "是否按比例承担",
  "joint_several_liability_flag": "是否承担连带责任",
  "joint_several_liability_subject": "连带责任承担主体",
}

basic_plan_contingent_liability_key_type_list = {
  "debt_scope": "textarea",
  "subject_name": "text",
  "subject_identity": "text",
  "prorated_commitment_flag": "checkbox",
  "joint_several_liability_flag": "checkbox",
  "joint_several_liability_subject": "textarea"
}

# 基本方案-交易完成后的整合-公司治理安排-table
basic_plan_integration_corporate_governance_arrangements_key_value_list = {
  "board_of_directors_composition": "董事会构成",
  "board_of_supervisors_composition": "监事会构成",
  "legal_representative": "法定代表人",
  "chairman": "董事长",
  "board_resolution_procedure": "董事会决议程序",
  "resolution_major_matters_procedures": "重大事项决议程序",
  "senior": "高级管理人员",
}

basic_plan_integration_corporate_governance_arrangements_key_type_list = {
  "board_of_directors_composition": "textarea",
  "board_of_supervisors_composition": "textarea",
  "legal_representative": "text",
  "chairman": "text",
  "board_resolution_procedure": "textarea",
  "resolution_major_matters_procedures": "textarea",
  "senior": "textarea"
}

# 交易完成后的整合-劳动关系-table
integration_labor_relations_key_value_list = {
  "subject": "主体",
  "identity": "身份",
  "labor_contract_term": "劳动合同期限",
  "prohibition_of_competition_term": "竞业禁止期限",
  "non_competition_starting_time": "竞业禁止开始时间",
  "non_competition_ending_time": "竞业禁止结束时间",
}

integration_labor_relations_key_type_list = {
  "subject": "text",
  "identity": "text",
  "labor_contract_term": "textarea",
  "prohibition_of_competition_term": "textarea",
  "non_competition_starting_time": "text",
  "non_competition_ending_time": "text"
}

# 交易完成后的整合-融资支持-table
integration_financing_support_key_value_list = {
  "support_mode": "支持方式",
  "support_amount": "支持金额",
  "support_conditions": "支持条件",
}

integration_financing_support_key_type_list = {
  "support_mode": "text",
  "support_amount": "text",
  "support_conditions": "textarea"
}

# 交易完成后的整合-财税安排-table
integration_fiscal_taxation_arrangements_key_value_list = {
  "finance": "财务",
  "taxation": "税务",
}

integration_fiscal_taxation_arrangements_key_type_list = {
  "finance": "textarea",
  "taxation": "textarea"
}

# 标的资产交易价格的调整-table
underlying_assets_transaction_price_adjustment_key_value_list = {
  "payment_object": "支付对象",
  "payment_object_identity": "支付对象身份",
  "trigger_condition": "触发条件",
  "underlying_assets_before_adjustment_price": "调整前标的资产的交易价格（万元）",
  "adjusted_underlying_assets_transaction_price": "调整后标的资产的交易价格（万元）",
  "adjusted_underlying_assets_transaction_price_increase": "调整后标的资产交易价格增加额（万元）",
  "adjusted_trading_price_determination_time": "调整后的交易价格确定时间",
  "adjusted_transaction_amount_payment_time": "调整后的交易金额支付时间",
  "cash_payment_amount": "现金支付金额",
  "share_payment_amount": "股份支付金额",
}

underlying_assets_transaction_price_adjustment_key_type_list = {
  "payment_object": "text",
  "payment_object_identity": "text",
  "trigger_condition": "textarea",
  "underlying_assets_before_adjustment_price": "decimal",
  "adjusted_underlying_assets_transaction_price": "decimal",
  "adjusted_underlying_assets_transaction_price_increase": "decimal",
  "adjusted_trading_price_determination_time": "textarea",
  "adjusted_transaction_amount_payment_time": "textarea",
  "cash_payment_amount": "text",
  "share_payment_amount": "text"
}

# 股份锁定期-table
share_lock_in_period_key_value_list = {
  "share_locks_subject": "股份锁定主体",
  "identity": "身份",
  "share_lock_in_period": "股份锁定期限",
  "new_transferable_share_number_during_lock_in_period": "锁定期内新增可转让股份数（股）",
  "new_transferable_share_in_lock_in_period_proportion": "锁定期内新增可转让股份所占比例（%）",
  "prolonged_locking_period": "锁定期延长情形",
  "share_deduction_with_compensation_obligation_flag": "是否存在补偿义务扣减股份数",
  "new_share_listing_time": "新增股份上市时间",
  "limited_shareto_sale_circulation_time": "限售股份解禁上市流通时间",
}

share_lock_in_period_key_type_list = {
  "share_locks_subject": "text",
  "identity": "text",
  "share_lock_in_period": "textarea",
  "new_transferable_share_number_during_lock_in_period": "int",
  "new_transferable_share_in_lock_in_period_proportion": "ratio",
  "prolonged_locking_period": "textarea",
  "share_deduction_with_compensation_obligation_flag": "checkbox",
  "new_share_listing_time": "textarea",
  "limited_shareto_sale_circulation_time": "textarea"
}

# 标的资产剩余股权的安排-table
residual_stocks_in_underlying_assets_arrangement_key_value_list = {
  "shareholder_holding_underlying_assets_remaining_stock": "持有标的资产剩余股权的股东",
  "shareholding_quantity": "持股数量（股）",
  "shareholding_ratio": "持股比例（%）",
  "residual_stock_follow_up_arrangement": "剩余股权后续安排",
  "remaining_stock_acquisition_time_arrangement": "剩余股权收购时间安排",
  "transaction_pricing": "交易作价",
  "payment": "支付方式",
}

residual_stocks_in_underlying_assets_arrangement_key_type_list = {
  "shareholder_holding_underlying_assets_remaining_stock": "text",
  "shareholding_quantity": "int",
  "shareholding_ratio": "ratio",
  "residual_stock_follow_up_arrangement": "textarea",
  "remaining_stock_acquisition_time_arrangement": "textarea",
  "transaction_pricing": "text",
  "payment": "text"
}

# 违约责任-table
breach_contract_liability_key_value_list = {
  "breach_of_contract_subject": "违约主体",
  "identity": "身份",
  "contract_breach": "违约行为",
  "default_type": "违约类型",
  "liquidated_damages_calculating_method": "违约金计算方式",
  "each_subject_joint_several_liabilities_flag": "各主体是否承担连带责任",
}

breach_contract_liability_key_type_list = {
  "breach_of_contract_subject": "text",
  "identity": "text",
  "contract_breach": "textarea",
  "default_type": "text",
  "liquidated_damages_calculating_method": "textarea",
  "each_subject_joint_several_liabilities_flag": "checkbox"
}

# 支付现金-定金-table
cash_payment_earnest_money_key_value_list = {
  "payment_object": "支付对象",
  "payment_object_identity": "支付对象身份",
  "deposit_amount": "定金数额（万元）",
  "deposit_ratio": "定金比例（%）",
  "payment_time": "支付时间",
}

cash_payment_earnest_money_key_type_list = {
  "payment_object": "text",
  "payment_object_identity": "text",
  "deposit_amount": "decimal",
  "deposit_ratio": "ratio",
  "payment_time": "text"
}

# 支付方式-现金支付-table
payment_cash_payment_key_value_list = {
  "counterparty_name": "交易对方名称",
  "counterparty_identity": "交易对方身份",
  "cash_payment_amount": "现金支付金额（万元）",
  "first_stage_payment_amount": "第一期支付金额（万元）",
  "first_payment_period": "第一期支付时间",
  "payment_in_second_instalment_amount": "第二期支付金额（万元）",
  "second_payment_period": "第二期支付时间",
  "payment_in_third_instalment_amount": "第三期支付金额（万元）",
  "third_payment_period": "第三期支付时间",
  "one_time_cash_payment_time": "一次性现金支付时间",
  "compensation_or_amount_of_compensation_deduction_flag": "是否先扣除补偿或赔偿金额",
}

payment_cash_payment_key_type_list = {
  "counterparty_name": "text",
  "counterparty_identity": "text",
  "cash_payment_amount": "decimal",
  "first_stage_payment_amount": "decimal",
  "first_payment_period": "text",
  "payment_in_second_instalment_amount": "decimal",
  "second_payment_period": "text",
  "payment_in_third_instalment_amount": "decimal",
  "third_payment_period": "text",
  "one_time_cash_payment_time": "text",
  "compensation_or_amount_of_compensation_deduction_flag": "checkbox"
}

# 支付现金—支付后二级市场购买股票安排-table
stock_purchase_arrangement_in_secondary_market_after_payment_key_value_list = {
  "buying_body": "购买主体",
  "purchaser_identity": "购买主体身份",
  "buying_time": "购买时间",
  "purchase_amount": "购买金额",
  "purchasing_ways": "购买方式",
  "purchase_share_lock_in_period_arrangement": "购买股份锁定期安排",
}

stock_purchase_arrangement_in_secondary_market_after_payment_key_type_list = {
  "buying_body": "text",
  "purchaser_identity": "text",
  "buying_time": "text",
  "purchase_amount": "textarea",
  "purchasing_ways": "textarea",
  "purchase_share_lock_in_period_arrangement": "textarea"
}

# 支付方式-发行股份-table
payment_issue_share_key_value_list = {
  "issue_object": "发行对象",
  "issuer_identity": "发行对象身份",
  "transaction_amount_purchased_by_issuing_share": "发行股份购买的交易金额（万元）",
  "issue_quantity": "发行数量(股)",
  "pricing_date": "定价基准日",
  "issue_price": "发行价格（元/股）",
}

payment_issue_share_key_type_list = {
  "issue_object": "text",
  "issuer_identity": "text",
  "transaction_amount_purchased_by_issuing_share": "decimal",
  "issue_quantity": "int",
  "pricing_date": "textarea",
  "issue_price": "decimal"
}

# 支付方式-发行股份-发行股份价格调整-table
payment_issue_share_share_price_adjustment_key_value_list = {
  "trigger_condition_type": "触发条件类型",
  "trigger_condition_content": "触发条件内容",
  "price_adjustment_date": "调价基准日",
  "adjustable_price_period": "可调价期间",
  "price_adjustment_mechanism": "价格调整机制",
  "pre_adjustment_issue_price": "调整前发行价格（元/股）",
  "adjusted_issue_price": "调整后发行价格（元/股）",
}

payment_issue_share_share_price_adjustment_key_type_list = {
  "trigger_condition_type": "text",
  "trigger_condition_content": "textarea",
  "price_adjustment_date": "textarea",
  "adjustable_price_period": "textarea",
  "price_adjustment_mechanism": "textarea",
  "pre_adjustment_issue_price": "decimal",
  "adjusted_issue_price": "decimal"
}

# 支付方式-发行定向可转债-table
payment_directional_convertible_bonds_issuance_key_value_list = {
  "issue_object": "发行对象",
  "issuer_identity": "发行对象身份",
  "target_companystock_ratio": "所持标的公司股权比例（%）",
  "bonds_payment_consideration_amount": "发行可转债支付对价金额（万元）",
  "issue_quantity": "发行数量(万张)",
  "bonds_convertible_quantity_at_initial_conversion_price": "可转换债券按初始转股价格可转股数量（股）",
  "issuing_mode": "发行方式",
  "bond_maturity": "债券期限",
  "stock_transfer_period": "转股期限",
  "bond_interest_rate": "债券利率",
  "interest_bearing_method": "计息方式",
  "setting_up_guarantee_flag": "是否设置担保",
  "conversion_price": "转股价格",
}

payment_directional_convertible_bonds_issuance_key_type_list = {
  "issue_object": "text",
  "issuer_identity": "text",
  "target_companystock_ratio": "ratio",
  "bonds_payment_consideration_amount": "decimal",
  "issue_quantity": "decimal",
  "bonds_convertible_quantity_at_initial_conversion_price": "int",
  "issuing_mode": "text",
  "bond_maturity": "textarea",
  "stock_transfer_period": "textarea",
  "bond_interest_rate": "textarea",
  "interest_bearing_method": "textarea",
  "setting_up_guarantee_flag": "checkbox",
  "conversion_price": "textarea"
}

# 支付方式-发行可转债-转股价格向下修正-form
payment_bonds_convertible_price_downward_revision_key_value_list = {
  "downward_revision_period": "向下修正期限",
  "price_conditions_downward_revision": "向下修正价格条件",
  "conversion_price_before_downward_amendment": "向下修正前的转股价格",
  "downward_modified_price_interval": "向下修正后的价格区间",
  "downward_modified_conversion_price": "向下修正后的转股价格",
  "downward_revisions_number": "向下修正次数",
  "price_scope_downward_modification": "向下修正价格适用范围",
  "downward_revision_procedure": "向下修正程序",
}

payment_bonds_convertible_price_downward_revision_key_type_list = {
  "downward_revision_period": "textarea",
  "price_conditions_downward_revision": "textarea",
  "conversion_price_before_downward_amendment": "textarea",
  "downward_modified_price_interval": "textarea",
  "downward_modified_conversion_price": "textarea",
  "downward_revisions_number": "text",
  "price_scope_downward_modification": "textarea",
  "downward_revision_procedure": ""
}

# 支付方式-发行可转债-转股价格向上修正-form
payment_bonds_conversion_price_upward_modification_key_value_list = {
  "upward_revision_period": "向上修正期限",
  "price_conditions_upward_modification": "向上修正价格条件",
  "conversion_price_before_upward_amendment": "向上修正前的转股价格",
  "upward_modified_price_interval": "向上修正后的价格区间",
  "upward_modified_conversion_price": "向上修正后的转股价格",
  "upward_revision_times": "向上修正次数",
  "price_scope_upward_modification": "向上修正价格适用范围",
  "upward_revision_procedure": "向上修正程序",
}

payment_bonds_conversion_price_upward_modification_key_type_list = {
  "upward_revision_period": "textarea",
  "price_conditions_upward_modification": "textarea",
  "conversion_price_before_upward_amendment": "textarea",
  "upward_modified_price_interval": "textarea",
  "upward_modified_conversion_price": "textarea",
  "upward_revision_times": "text",
  "price_scope_upward_modification": "textarea",
  "upward_revision_procedure": "textarea"
}

# 支付方式-发行可转债-提前回售-form
payment_bonds_early_resale_key_value_list = {
  "pre_sale_conditions": "提前回售条件",
  "pre_sale_method": "提前回售方式",
  "exercise_period": "行权期",
  "interest_on_unsold_part_calculation": "未回售部分利息计算",
}

payment_bonds_early_resale_key_type_list = {
  "pre_sale_conditions": "textarea",
  "pre_sale_method": "textarea",
  "exercise_period": "textarea",
  "interest_on_unsold_part_calculation": "textarea"
}

# 支付方式-发行可转债-强制转股-form
payment_bonds_compulsory_equity_swap_key_value_list = {
  "mandatory_equity_swap_conditions": "强制转股条件",
  "compulsory_share_conversion_procedure": "强制转股程序",
}

payment_bonds_compulsory_equity_swap_key_type_list = {
  "mandatory_equity_swap_conditions": "textarea",
  "compulsory_share_conversion_procedure": "textarea"
}

# 发行股份及募集配套资金基本概况-table
issuing_share_raising_matching_funds_basic_situation_key_value_list = {
  "distribution_object_name": "发行对象名称",
  "issuer_identity": "发行对象身份",
  "raising_matching_funds": "募集配套资金额（万元）",
  "issue_quantity": "发行数量(股)",
  "pricing_date": "定价基准日",
  "issue_price": "发行价格（元/股）",
  "payment": "支付方式",
  "issuing_mode": "发行方式",
  "merger_acquisition_bottom_price_matching_financing": "并购配套融资发行底价",
  "merger_acquisition_matching_financing_price": "并购配套融资发行价格",
  "issuance_price_over_issuance_base_price_floating_rate": "发行价格较发行底价上浮率（%）",
  "next_day_sfc_approves_closing_price": "证监会核准次日收盘价",
  "issuance_price_over_approved_next_day_discount_rate": "发行价格较核准次日折价率（%）",
  "date_of_securities_regulatory_commission_average_daily_price": "证监核准日前20个交易日均价",
  "sfc_issuance_price_two0_days_before_approval": "发行价格较证监会核准前20日均价折价率（%）",
  "share_lock_in_period": "股份锁定期",
}

issuing_share_raising_matching_funds_basic_situation_key_type_list = {
  "distribution_object_name": "text",
  "issuer_identity": "text",
  "raising_matching_funds": "text",
  "issue_quantity": "text",
  "pricing_date": "textarea",
  "issue_price": "textarea",
  "payment": "text",
  "issuing_mode": "text",
  "merger_acquisition_bottom_price_matching_financing": "textarea",
  "merger_acquisition_matching_financing_price": "textarea",
  "issuance_price_over_issuance_base_price_floating_rate": "textarea",
  "next_day_sfc_approves_closing_price": "textarea",
  "issuance_price_over_approved_next_day_discount_rate": "textarea",
  "date_of_securities_regulatory_commission_average_daily_price": "textarea",
  "sfc_issuance_price_two0_days_before_approval": "textarea",
  "share_lock_in_period": "text"
}

# 资产评估-基础数据-form
assets_appraisal_basic_data_key_value_list = {
  "assessment_method": "评估方法",
  "assessment_baseline_date": "评估基准日",
  "supplementary_assessment_baseline_date": "补充评估基准日",
  "book_net_assets": "账面净资产（万元）",
  "assessment_results": "评估结果（万元）",
  "evaluation_increment": "评估增值（万元）",
  "appreciation_rate": "增值率（%）",
  "applying_methods_to_evaluate_results": "评估结果采用方法",
  "transaction_price": "交易价格（万元）",
  "transaction_value_added_rate": "交易增值率（%）",
}

assets_appraisal_basic_data_key_type_list = {
  "assessment_method": "text",
  "assessment_baseline_date": "datetime",
  "supplementary_assessment_baseline_date": "datetime",
  "book_net_assets": "decimal",
  "assessment_results": "decimal",
  "evaluation_increment": "decimal",
  "appreciation_rate": "ratio",
  "applying_methods_to_evaluate_results": "text",
  "transaction_price": "decimal",
  "transaction_value_added_rate": "text"
}

# 标的资产的财务数据-form
underlying_assets_financial_data_key_value_list = {
  "reporting_period_first_year": "报告期第一年年度",
  "first_year_reporting_period_audited_net_profit": "报告期第一年经审计的净利润（万元）",
  "reporting_period_second_year": "报告期第二年年度",
  "year_underlying_assets_reporting_period_audited_net_profit": "标的资产报告期第二年经审计的净利润（万元）",
  "reporting_period_period_i": "报告期一期期间",
  "understanding_assets_reporting_period_audited_net_profit": "标的资产报告期一期经审计的净利润（万元）",
  "annual_declaration": "申报当年年度",
  "year_underlying_assets_declare_performance_commitment": "标的资产申报当年的业绩承诺（万元）",
  "audited_in_year_before_it_was_declared_performance_commitment": "标的资产申报当年的业绩承诺比申报前一年经审计的净利润增加数",
  "first_year_after_declaration": "申报后第一年年度",
  "performance_commitment_number_in_first_year_after_declaration": "申报后第一年业绩承诺数（万元）",
  "actually_achieved_in_first_year_after_declaration_number": "申报后第一年实际实现的业绩数（万元）",
  "to_commitment_in_first_year_after_declaration_proportion": "申报后第一年实际实现的业绩数占承诺数的比例（%）",
  "year_two_after_declaration": "申报后第二年年度",
  "performance_commitment_number_in_second_year_after_declaration": "申报后第二年年度业绩承诺数（万元）",
  "actual_achievements_in_second_year_after_declaration": "申报后第二年实际实现的业绩数（万元）",
  "to_commitment_in_second_year_after_declaration_ratio": "申报后第二年实际实现的业绩数占承诺数的比例（%）",
  "year_three_after_declaration": "申报后第三年年度",
  "annual_performance_commitment_in_third_year_after_declaration": "申报后第三年年度业绩承诺（万元）",
  "actual_achievements_in_third_year_after_declaration": "申报后第三年实际实现的业绩数（万元）",
  "to_commitment_in_third_year_after_declaration_ratio": "申报后第三年实际实现的业绩数占承诺数的比例（%）",
  "fourth_year_after_declaration": "申报后第四年年度",
  "annual_performance_commitment_in_fourth_year_after_declaration": "申报后第四年年度业绩承诺（万元）",
  "actual_achievements_in_fourth_year_after_declaration": "申报后第四年实际实现的业绩数（万元）",
  "to_commitment_in_fourth_year_after_declaration_proportion": "申报后第四年实际实现的业绩数占承诺数的比例（%）",
}

underlying_assets_financial_data_key_type_list = {
  "reporting_period_first_year": "text",
  "first_year_reporting_period_audited_net_profit": "decimal",
  "reporting_period_second_year": "text",
  "year_underlying_assets_reporting_period_audited_net_profit": "decimal",
  "reporting_period_period_i": "text",
  "understanding_assets_reporting_period_audited_net_profit": "decimal",
  "annual_declaration": "text",
  "year_underlying_assets_declare_performance_commitment": "text",
  "audited_in_year_before_it_was_declared_performance_commitment": "text",
  "first_year_after_declaration": "text",
  "performance_commitment_number_in_first_year_after_declaration": "text",
  "actually_achieved_in_first_year_after_declaration_number": "text",
  "to_commitment_in_first_year_after_declaration_proportion": "text",
  "year_two_after_declaration": "text",
  "performance_commitment_number_in_second_year_after_declaration": "text",
  "actual_achievements_in_second_year_after_declaration": "text",
  "to_commitment_in_second_year_after_declaration_ratio": "text",
  "year_three_after_declaration": "text",
  "annual_performance_commitment_in_third_year_after_declaration": "text",
  "actual_achievements_in_third_year_after_declaration": "text",
  "to_commitment_in_third_year_after_declaration_ratio": "text",
  "fourth_year_after_declaration": "text",
  "annual_performance_commitment_in_fourth_year_after_declaration": "text",
  "actual_achievements_in_fourth_year_after_declaration": "text",
  "to_commitment_in_fourth_year_after_declaration_proportion": "text"
}

# 交易市盈率-form
trading_pe_key_value_list = {
  "year_before_declaration_static_pe_ratio": "申报前一年静态市盈率",
  "annual_declaration": "申报当年年度",
  "declare_current_year_dynamic_pe_ratio": "申报当年动态市盈率",
  "year_two_after_declaration": "申报后第二年年度",
  "dynamic_pe_ratio_in_second_year_after_declaration": "申报后第二年动态市盈率",
  "year_three_after_declaration": "申报后第三年年度",
  "dynamic_pe_ratio_in_third_year_after_declaration": "申报后第三年动态市盈率",
  "fourth_year_after_declaration": "申报后第四年年度",
  "dynamic_pe_ratio_in_fourth_year_after_declaration": "申报后第四年动态市盈率",
}

trading_pe_key_type_list = {
  "year_before_declaration_static_pe_ratio": "decimal",
  "annual_declaration": "text",
  "declare_current_year_dynamic_pe_ratio": "text",
  "year_two_after_declaration": "text",
  "dynamic_pe_ratio_in_second_year_after_declaration": "text",
  "year_three_after_declaration": "text",
  "dynamic_pe_ratio_in_third_year_after_declaration": "text",
  "fourth_year_after_declaration": "text",
  "dynamic_pe_ratio_in_fourth_year_after_declaration": "text"
}

# 业绩承诺安排-form
performance_commitment_arrangement_key_value_list = {
  "performance_commitment_arrangement_committed_person": "业绩承诺安排-承诺人",
  "identity": "身份",
  "shareholding_ratio": "持股比例（%）",
}

performance_commitment_arrangement_key_type_list = {
  "performance_commitment_arrangement_committed_person": "text",
  "identity": "text",
  "shareholding_ratio": "ratio"
}

# 业绩承诺安排-承诺期间-form
performance_commitment_arrangement_commitment_period_key_value_list = {
  "committed_person": "承诺人",
  "identity": "身份",
  "three_years_flag": "三年",
  "four_years_flag": "四年",
  "specific_year": "具体年度",
  "duration_extension_flag": "是否存在期间顺延",
}

performance_commitment_arrangement_commitment_period_key_type_list = {
  "committed_person": "text",
  "identity": "text",
  "three_years_flag": "checkbox",
  "four_years_flag": "checkbox",
  "specific_year": "text",
  "duration_extension_flag": "checkbox"
}

# 业绩承诺安排-承诺业绩-form
performance_commitment_arrangement_committed_performance_key_value_list = {
  "committed_person": "承诺人",
  "identity": "身份",
  "commitment_to_net_profit_flag": "承诺净利润",
  "commitment_to_net_operating_cash_flow": "承诺经营性现金流量净额",
  "commitment_to_sign_contract_amount": "承诺签订合同金额",
  "committed_inventory_flag": "承诺存货",
  "commitment_to_accounts_receivable_flag": "承诺应收账款",
  "commitment_to_long_term_receivables_flag": "承诺长期应收款",
}

performance_commitment_arrangement_committed_performance_key_type_list = {
  "committed_person": "text",
  "identity": "text",
  "commitment_to_net_profit_flag": "checkbox",
  "commitment_to_net_operating_cash_flow": "text",
  "commitment_to_sign_contract_amount": "text",
  "committed_inventory_flag": "checkbox",
  "commitment_to_accounts_receivable_flag": "checkbox",
  "commitment_to_long_term_receivables_flag": "checkbox"
}

# 业绩承诺安排-承诺业绩-承诺净利润-table
arrangement_committed_performance_commitment_to_net_profit_key_value_list = {
  "first_year": "第一年",
  "first_year_commitment_to_net_profit": "第一年承诺净利润（万元）",
  "second_years": "第二年",
  "second_year_commitment_net_profit": "第二年承诺净利润（万元）",
  "third_year": "第三年",
  "third_year_commitment_net_profit": "第三年承诺净利润（万元）",
  "fourth_years": "第四年",
  "fourth_year_commitment_net_profit": "第四年承诺净利润（万元）",
  "accumulated_commitment_net_profit": "累计承诺净利润（万元）",
  "actual_performance_audit": "实际业绩审计",
  "how_to_determine_accounting_firms": "会计师事务所确定方式",
}

arrangement_committed_performance_commitment_to_net_profit_key_type_list = {
  "first_year": "text",
  "first_year_commitment_to_net_profit": "decimal",
  "second_years": "text",
  "second_year_commitment_net_profit": "decimal",
  "third_year": "text",
  "third_year_commitment_net_profit": "decimal",
  "fourth_years": "text",
  "fourth_year_commitment_net_profit": "decimal",
  "accumulated_commitment_net_profit": "decimal",
  "actual_performance_audit": "text",
  "how_to_determine_accounting_firms": "text"
}

# 业绩承诺安排-承诺业绩-承诺经营性现金流量净额-table
committed_performance_commitment_to_net_operating_cash_flow_key_value_list = {
  "first_year": "第一年",
  "net_operating_cash_flow_promised_in_first_year": "第一年承诺经营性现金流量净额（万元）",
  "second_years": "第二年",
  "second_year_net_operating_cash_flow_promised": "第二年承诺经营性现金流量净额（万元）",
  "third_year": "第三年",
  "third_year_net_operating_cash_flow_promised": "第三年承诺经营性现金流量净额（万元）",
  "fourth_years": "第四年",
  "fourth_year_net_operating_cash_flow_promised": "第四年承诺经营性现金流量净额（万元）",
  "accumulated_net_operating_cash_flow_commitment": "累计承诺经营性现金流量净额（万元）",
  "actual_performance_audit": "实际业绩审计",
  "how_to_determine_accounting_firms": "会计师事务所确定方式",
}

committed_performance_commitment_to_net_operating_cash_flow_key_type_list = {
  "first_year": "text",
  "net_operating_cash_flow_promised_in_first_year": "decimal",
  "second_years": "text",
  "second_year_net_operating_cash_flow_promised": "decimal",
  "third_year": "text",
  "third_year_net_operating_cash_flow_promised": "decimal",
  "fourth_years": "text",
  "fourth_year_net_operating_cash_flow_promised": "decimal",
  "accumulated_net_operating_cash_flow_commitment": "decimal",
  "actual_performance_audit": "text",
  "how_to_determine_accounting_firms": "text"
}

# 业绩承诺安排-承诺业绩-承诺签订合同金额-table
committed_performance_commitment_to_sign_contract_amount_key_value_list = {
  "first_year": "第一年",
  "contract_promised_in_first_year_amount": "第一年承诺签订合同金额（万元）",
  "second_years": "第二年",
  "contract_promised_in_second_year_amount": "第二年承诺签订合同金额（万元）",
  "third_year": "第三年",
  "contract_promised_in_third_year_amount": "第三年承诺签订合同金额（万元）",
  "fourth_years": "第四年",
  "contract_promised_in_fourth_year_amount": "第四年承诺签订合同金额（万元）",
  "accumulative_undertaking_to_sign_contract": "累计承诺签订合同金额（万元）",
  "actual_performance_audit": "实际业绩审计",
  "how_to_determine_accounting_firms": "会计师事务所确定方式",
}

committed_performance_commitment_to_sign_contract_amount_key_type_list = {
  "first_year": "text",
  "contract_promised_in_first_year_amount": "decimal",
  "second_years": "text",
  "contract_promised_in_second_year_amount": "decimal",
  "third_year": "text",
  "contract_promised_in_third_year_amount": "decimal",
  "fourth_years": "text",
  "contract_promised_in_fourth_year_amount": "decimal",
  "accumulative_undertaking_to_sign_contract": "decimal",
  "actual_performance_audit": "text",
  "how_to_determine_accounting_firms": "text"
}

# 业绩承诺安排-承诺业绩-承诺存货-table
arrangement_committed_performance_committed_inventory_key_value_list = {
  "recovery_time": "回收时间",
}

arrangement_committed_performance_committed_inventory_key_type_list = {
  "recovery_time": "text"
}

# 业绩承诺安排-承诺业绩-承诺存货-回收率-table
committed_performance_committed_inventory_recovery_rate_key_value_list = {
  "first_year": "第一年",
  "first_year_commitment_inventory_recovery_rate": "第一年承诺存货回收率（%）",
  "second_years": "第二年",
  "second_year_commitment_inventory_recovery_rate": "第二年承诺存货回收率（%）",
  "third_year": "第三年",
  "third_year_commitment_inventory_recovery_rate": "第三年承诺存货回收率（%）",
  "fourth_years": "第四年",
  "fourth_year_commitment_inventory_recovery_rate": "第四年承诺存货回收率（%）",
  "actual_performance_audit": "实际业绩审计",
  "how_to_determine_accounting_firms": "会计师事务所确定方式",
}

committed_performance_committed_inventory_recovery_rate_key_type_list = {
  "first_year": "text",
  "first_year_commitment_inventory_recovery_rate": "ratio",
  "second_years": "text",
  "second_year_commitment_inventory_recovery_rate": "ratio",
  "third_year": "text",
  "third_year_commitment_inventory_recovery_rate": "ratio",
  "fourth_years": "text",
  "fourth_year_commitment_inventory_recovery_rate": "ratio",
  "actual_performance_audit": "text",
  "how_to_determine_accounting_firms": "text"
}

# 业绩承诺安排-承诺业绩-承诺存货-周转率-table
committed_performance_committed_inventory_turnover_rate_key_value_list = {
  "first_year": "第一年",
  "first_year_commitment_inventory_turnover_rate": "第一年承诺存货周转率",
  "second_years": "第二年",
  "second_year_commitment_inventory_turnover_rate": "第二年承诺存货周转率",
  "third_year": "第三年",
  "third_year_commitment_inventory_turnover_rate": "第三年承诺存货周转率",
  "fourth_years": "第四年",
  "fourth_year_commitment_inventory_turnover_rate": "第四年承诺存货周转率",
  "actual_performance_audit": "实际业绩审计",
  "how_to_determine_accounting_firms": "会计师事务所确定方式",
}

committed_performance_committed_inventory_turnover_rate_key_type_list = {
  "first_year": "text",
  "first_year_commitment_inventory_turnover_rate": "decimal",
  "second_years": "text",
  "second_year_commitment_inventory_turnover_rate": "decimal",
  "third_year": "text",
  "third_year_commitment_inventory_turnover_rate": "decimal",
  "fourth_years": "text",
  "fourth_year_commitment_inventory_turnover_rate": "decimal",
  "actual_performance_audit": "text",
  "how_to_determine_accounting_firms": "text"
}

# 业绩承诺安排-承诺业绩-承诺应收账款-table
committed_performance_commitment_to_accounts_receivable_key_value_list = {
  "recovery_time": "回收时间",
}

committed_performance_commitment_to_accounts_receivable_key_type_list = {
  "recovery_time": "text"
}

# 业绩承诺安排-承诺业绩-承诺应收账款-回收率-table
performance_commitment_to_accounts_receivable_recovery_rate_key_value_list = {
  "first_year": "第一年",
  "first_year_commitment_receivables_recovery_ratio": "第一年承诺应收账款回收率（%）",
  "second_years": "第二年",
  "second_year_commitment_receivables_recovery_ratio": "第二年承诺应收账款回收率（%）",
  "third_year": "第三年",
  "third_year_commitment_receivables_recovery_ratio": "第三年承诺应收账款回收率（%）",
  "fourth_years": "第四年",
  "fourth_year_commitment_receivables_recovery_ratio": "第四年承诺应收账款回收率（%）",
  "actual_performance_audit": "实际业绩审计",
  "how_to_determine_accounting_firms": "会计师事务所确定方式",
}

performance_commitment_to_accounts_receivable_recovery_rate_key_type_list = {
  "first_year": "text",
  "first_year_commitment_receivables_recovery_ratio": "ratio",
  "second_years": "text",
  "second_year_commitment_receivables_recovery_ratio": "ratio",
  "third_year": "text",
  "third_year_commitment_receivables_recovery_ratio": "ratio",
  "fourth_years": "text",
  "fourth_year_commitment_receivables_recovery_ratio": "ratio",
  "actual_performance_audit": "text",
  "how_to_determine_accounting_firms": "text"
}

# 业绩承诺安排-承诺业绩-承诺应收账款-周转率-table
performance_commitment_to_accounts_receivable_turnover_rate_key_value_list = {
  "first_year": "第一年",
  "first_year_commitment_receivables_turnover_rate": "第一年承诺应收账款周转率",
  "second_years": "第二年",
  "second_year_commitment_receivable_turnover_rate": "第二年承诺应收账款周转率",
  "third_year": "第三年",
  "third_year_commitment_receivable_turnover_rate": "第三年承诺应收账款周转率",
  "fourth_years": "第四年",
  "fourth_year_commitment_receivable_turnover_rate": "第四年承诺应收账款周转率",
  "actual_performance_audit": "实际业绩审计",
  "how_to_determine_accounting_firms": "会计师事务所确定方式",
}

performance_commitment_to_accounts_receivable_turnover_rate_key_type_list = {
  "first_year": "text",
  "first_year_commitment_receivables_turnover_rate": "decimal",
  "second_years": "text",
  "second_year_commitment_receivable_turnover_rate": "decimal",
  "third_year": "text",
  "third_year_commitment_receivable_turnover_rate": "decimal",
  "fourth_years": "text",
  "fourth_year_commitment_receivable_turnover_rate": "decimal",
  "actual_performance_audit": "text",
  "how_to_determine_accounting_firms": "text"
}

# 业绩承诺安排-承诺业绩-承诺长期应收款-table
committed_performance_commitment_to_long_term_receivables_key_value_list = {
  "recovery_time": "回收时间",
}

committed_performance_commitment_to_long_term_receivables_key_type_list = {
  "recovery_time": "text"
}

# 业绩承诺安排-承诺业绩-承诺长期应收款-回收率-table
performance_commitment_to_long_term_receivables_recovery_rate_key_value_list = {
  "first_year": "第一年",
  "first_year_commitment_long_term_recovery_ratio": "第一年承诺长期应收款回收率（%）",
  "second_years": "第二年",
  "second_year_commitment_long_term_recovery_ratio": "第二年承诺长期应收款回收率（%）",
  "third_year": "第三年",
  "third_year_commitment_long_term_recovery_ratio": "第三年承诺长期应收款回收率（%）",
  "fourth_years": "第四年",
  "fourth_year_commitment_long_term_recovery_ratio": "第四年承诺长期应收款回收率（%）",
  "actual_performance_audit": "实际业绩审计",
  "how_to_determine_accounting_firms": "会计师事务所确定方式",
}

performance_commitment_to_long_term_receivables_recovery_rate_key_type_list = {
  "first_year": "text",
  "first_year_commitment_long_term_recovery_ratio": "ratio",
  "second_years": "text",
  "second_year_commitment_long_term_recovery_ratio": "ratio",
  "third_year": "text",
  "third_year_commitment_long_term_recovery_ratio": "ratio",
  "fourth_years": "text",
  "fourth_year_commitment_long_term_recovery_ratio": "ratio",
  "actual_performance_audit": "text",
  "how_to_determine_accounting_firms": "text"
}

# 业绩承诺安排-承诺业绩-承诺长期应收款-周转率-table
performance_commitment_to_long_term_receivables_turnover_rate_key_value_list = {
  "first_year": "第一年",
  "first_year_commit_long_term_turnover_ratio": "第一年承诺长期应收款周转率",
  "second_years": "第二年",
  "second_year_commit_long_term_turnover_ratio": "第二年承诺长期应收款周转率",
  "third_year": "第三年",
  "third_year_commit_long_term_turnover_ratio": "第三年承诺长期应收款周转率",
  "fourth_years": "第四年",
  "fourth_year_commit_long_term_turnover_ratio": "第四年承诺长期应收款周转率",
  "actual_performance_audit": "实际业绩审计",
  "how_to_determine_accounting_firms": "会计师事务所确定方式",
}

performance_commitment_to_long_term_receivables_turnover_rate_key_type_list = {
  "first_year": "text",
  "first_year_commit_long_term_turnover_ratio": "decimal",
  "second_years": "text",
  "second_year_commit_long_term_turnover_ratio": "decimal",
  "third_year": "text",
  "third_year_commit_long_term_turnover_ratio": "decimal",
  "fourth_years": "text",
  "fourth_year_commit_long_term_turnover_ratio": "decimal",
  "actual_performance_audit": "text",
  "how_to_determine_accounting_firms": "text"
}

# 业绩承诺安排-承诺业绩计算标准-form
arrangement_commitment_performance_computing_criteria_key_value_list = {
  "deduction_items_type": "扣除项目类型",
  "realized_in_current_period_can_be_included_in_next_period": "当期实现的超额是否可以计入下一期",
  "financial_statements_basfor_preparation": "财物报表编制依据",
}

arrangement_commitment_performance_computing_criteria_key_type_list = {
  "deduction_items_type": "text",
  "realized_in_current_period_can_be_included_in_next_period": "text",
  "financial_statements_basfor_preparation": "text"
}

# 业绩预测补偿-form
performance_forecast_compensation_key_value_list = {
  "compensatory_obligor": "补偿义务人",
  "identity": "身份",
  "stock_ratio": "股权比例（%）",
  "compensation_period": "补偿期间",
  "compensation_obligation_triggering_conditions": "补偿义务触发条件",
  "compensation_amount": "补偿金额",
  "compensation_mode": "补偿方式",
  "exemption_from_obligation_to_compensate": "补偿义务豁免",
}

performance_forecast_compensation_key_type_list = {
  "compensatory_obligor": "text",
  "identity": "text",
  "stock_ratio": "ratio",
  "compensation_period": "text",
  "compensation_obligation_triggering_conditions": "textarea",
  "compensation_amount": "text",
  "compensation_mode": "text",
  "exemption_from_obligation_to_compensate": "text"
}

# 业绩预测补偿-补偿期间-table
performance_forecast_compensation_compensation_period_key_value_list = {
  "each_year_performance_commitment_period_flag": "业绩承诺期内每一年度",
  "performance_commitment_year_flag": "业绩承诺年度",
  "after_cumulative_performance_commitment_period_expires_flag": "累计业绩承诺期期满后",
}

performance_forecast_compensation_compensation_period_key_type_list = {
  "each_year_performance_commitment_period_flag": "checkbox",
  "performance_commitment_year_flag": "checkbox",
  "after_cumulative_performance_commitment_period_expires_flag": "checkbox"
}

# 业绩预测补偿-补偿金额-table
performance_forecast_compensation_compensation_amount_key_value_list = {
  "balance_compensation_flag": "差额补偿",
  "premium_compensation_flag": "溢价补偿",
  "commitment_indicators_types": "承诺指标类型",
  "compensation_calculation_formula": "补偿计算公式",
  "compensation_upper_limit": "补偿上限",
}

performance_forecast_compensation_compensation_amount_key_type_list = {
  "balance_compensation_flag": "checkbox",
  "premium_compensation_flag": "checkbox",
  "commitment_indicators_types": "text",
  "compensation_calculation_formula": "textarea",
  "compensation_upper_limit": "textarea"
}

# 业绩预测补偿-补偿方式-承诺净利润/经营性现金流量金额/签订合同金额-form
commitment_net_profit_operational_cash_flow_contract_amount_key_value_list = {
  "compensatory_obligor": "补偿义务人",
  "identity": "身份",
  "share_compensation_flag": "股份补偿",
  "cash_compensation_flag": "现金补偿",
  "share_or_cash_compensation_flag": "股份或现金补偿",
  "other_assets_recognized_by_listed_companies_compensation": "上市公司认可的其他资产补偿",
}

commitment_net_profit_operational_cash_flow_contract_amount_key_type_list = {
  "compensatory_obligor": "text",
  "identity": "text",
  "share_compensation_flag": "checkbox",
  "cash_compensation_flag": "checkbox",
  "share_or_cash_compensation_flag": "checkbox",
  "other_assets_recognized_by_listed_companies_compensation": "textarea"
}

# 业绩预测补偿-补偿方式-承诺净利润/经营性现金流量金额/签订合同金额-股份补偿-form
operational_cash_flow_contract_amount_share_compensation_key_value_list = {
  "compensatory_obligor": "补偿义务人",
  "identity": "身份",
  "share_compensation_trigger_condition": "股份补偿触发条件",
  "share_compensation_upper_limit": "股份补偿上限",
  "in_target_company_compensation_according_to_proportion_flag": "补偿义务分配-按在标的公司持股比例补偿",
  "in_proportion_to_shareholding_in_listed_companies_flag": "补偿义务分配-按在上市公司持股比例补偿",
  "compensation_compensation_in_other_proportions": "补偿义务分配-按其他比例补偿",
  "joint_several_compensation_flag": "连带补偿",
  "supplementary_compensation_flag": "补充补偿",
  "share_quantity_calculating_method_should_be_compensated": "应补偿股份数量计算方式",
  "share_quantity_adjustment_should_be_compensated": "应补偿股份数量调整",
}

operational_cash_flow_contract_amount_share_compensation_key_type_list = {
  "compensatory_obligor": "text",
  "identity": "text",
  "share_compensation_trigger_condition": "textarea",
  "share_compensation_upper_limit": "textarea",
  "in_target_company_compensation_according_to_proportion_flag": "checkbox",
  "in_proportion_to_shareholding_in_listed_companies_flag": "checkbox",
  "compensation_compensation_in_other_proportions": "textarea",
  "joint_several_compensation_flag": "checkbox",
  "supplementary_compensation_flag": "checkbox",
  "share_quantity_calculating_method_should_be_compensated": "textarea",
  "share_quantity_adjustment_should_be_compensated": "textarea"
}

# 业绩预测补偿-补偿方式-承诺净利润/经营性现金流量金额/签订合同金额-现金补偿-form
profit_operational_cash_flow_contract_amount_cash_compensation_key_value_list = {
  "compensatory_obligor": "补偿义务人",
  "identity": "身份",
  "cash_compensation_trigger_conditions": "现金补偿触发条件",
  "cash_compensation_ceiling": "现金补偿上限",
  "in_target_company_compensation_according_to_proportion_flag": "补偿义务分配-按在标的公司持股比例补偿",
  "in_proportion_to_shareholding_in_listed_companies_flag": "补偿义务分配-按在上市公司持股比例补偿",
  "compensation_compensation_in_other_proportions": "补偿义务分配-按其他比例补偿",
  "joint_several_compensation_flag": "连带补偿",
  "supplementary_compensation_flag": "补充补偿",
  "calculating_amount_of_compensable_cash_method": "应补偿现金金额计算方式",
  "compensable_cash_amount_adjustment": "应补偿现金金额调整",
}

profit_operational_cash_flow_contract_amount_cash_compensation_key_type_list = {
  "compensatory_obligor": "text",
  "identity": "text",
  "cash_compensation_trigger_conditions": "textarea",
  "cash_compensation_ceiling": "textarea",
  "in_target_company_compensation_according_to_proportion_flag": "checkbox",
  "in_proportion_to_shareholding_in_listed_companies_flag": "checkbox",
  "compensation_compensation_in_other_proportions": "textarea",
  "joint_several_compensation_flag": "checkbox",
  "supplementary_compensation_flag": "checkbox",
  "calculating_amount_of_compensable_cash_method": "textarea",
  "compensable_cash_amount_adjustment": "textarea"
}

# 业绩预测补偿-补偿方式-承诺存货-form
forecast_compensation_compensation_mode_committed_inventory_key_value_list = {
  "compensatory_obligor": "补偿义务人",
  "identity": "身份",
  "cash_compensation_flag": "现金补偿",
  "cash_compensation_trigger_conditions": "现金补偿触发条件",
  "cash_compensation_ceiling": "现金补偿上限",
  "in_target_company_compensation_according_to_proportion_flag": "补偿义务分配-按在标的公司持股比例补偿",
  "in_proportion_to_shareholding_in_listed_companies_flag": "补偿义务分配-按在上市公司持股比例补偿",
  "compensation_compensation_in_other_proportions": "补偿义务分配-按其他比例补偿",
  "joint_several_compensation_flag": "连带补偿",
  "supplementary_compensation_flag": "补充补偿",
  "calculating_amount_of_compensable_cash_method": "应补偿现金金额计算方式",
  "compensable_cash_amount_adjustment": "应补偿现金金额调整",
  "other_assets_recognized_by_listed_companies_compensation": "上市公司认可的其他资产补偿",
}

forecast_compensation_compensation_mode_committed_inventory_key_type_list = {
  "compensatory_obligor": "text",
  "identity": "text",
  "cash_compensation_flag": "checkbox",
  "cash_compensation_trigger_conditions": "textarea",
  "cash_compensation_ceiling": "textarea",
  "in_target_company_compensation_according_to_proportion_flag": "checkbox",
  "in_proportion_to_shareholding_in_listed_companies_flag": "checkbox",
  "compensation_compensation_in_other_proportions": "textarea",
  "joint_several_compensation_flag": "checkbox",
  "supplementary_compensation_flag": "checkbox",
  "calculating_amount_of_compensable_cash_method": "textarea",
  "compensable_cash_amount_adjustment": "textarea",
  "other_assets_recognized_by_listed_companies_compensation": "textarea"
}

# 业绩预测补偿-补偿方式-应收账款-form
forecast_compensation_compensation_mode_accounts_receivable_key_value_list = {
  "compensatory_obligor": "补偿义务人",
  "identity": "身份",
  "cash_compensation_flag": "现金补偿",
  "cash_compensation_trigger_conditions": "现金补偿触发条件",
  "cash_compensation_ceiling": "现金补偿上限",
  "in_target_company_compensation_according_to_proportion_flag": "补偿义务分配-按在标的公司持股比例补偿",
  "in_proportion_to_shareholding_in_listed_companies_flag": "补偿义务分配-按在上市公司持股比例补偿",
  "compensation_compensation_in_other_proportions": "补偿义务分配-按其他比例补偿",
  "joint_several_compensation_flag": "连带补偿",
  "supplementary_compensation_flag": "补充补偿",
  "calculating_amount_of_compensable_cash_method": "应补偿现金金额计算方式",
  "compensable_cash_amount_adjustment": "应补偿现金金额调整",
  "other_assets_recognized_by_listed_companies_compensation": "上市公司认可的其他资产补偿",
}

forecast_compensation_compensation_mode_accounts_receivable_key_type_list = {
  "compensatory_obligor": "text",
  "identity": "text",
  "cash_compensation_flag": "checkbox",
  "cash_compensation_trigger_conditions": "textarea",
  "cash_compensation_ceiling": "textarea",
  "in_target_company_compensation_according_to_proportion_flag": "checkbox",
  "in_proportion_to_shareholding_in_listed_companies_flag": "checkbox",
  "compensation_compensation_in_other_proportions": "textarea",
  "joint_several_compensation_flag": "checkbox",
  "supplementary_compensation_flag": "checkbox",
  "calculating_amount_of_compensable_cash_method": "textarea",
  "compensable_cash_amount_adjustment": "textarea",
  "other_assets_recognized_by_listed_companies_compensation": "textarea"
}

# 业绩预测补偿-补偿方式-长期应收款-form
forecast_compensation_compensation_mode_long_term_receivables_key_value_list = {
  "compensatory_obligor": "补偿义务人",
  "identity": "身份",
  "cash_compensation_flag": "现金补偿",
  "cash_compensation_trigger_conditions": "现金补偿触发条件",
  "cash_compensation_ceiling": "现金补偿上限",
  "in_target_company_compensation_according_to_proportion_flag": "补偿义务分配-按在标的公司持股比例补偿",
  "in_proportion_to_shareholding_in_listed_companies_flag": "补偿义务分配-按在上市公司持股比例补偿",
  "compensation_compensation_in_other_proportions": "补偿义务分配-按其他比例补偿",
  "joint_several_compensation_flag": "连带补偿",
  "supplementary_compensation_flag": "补充补偿",
  "calculating_amount_of_compensable_cash_method": "应补偿现金金额计算方式",
  "compensable_cash_amount_adjustment": "应补偿现金金额调整",
  "other_assets_recognized_by_listed_companies_compensation": "上市公司认可的其他资产补偿",
}

forecast_compensation_compensation_mode_long_term_receivables_key_type_list = {
  "compensatory_obligor": "text",
  "identity": "text",
  "cash_compensation_flag": "checkbox",
  "cash_compensation_trigger_conditions": "textarea",
  "cash_compensation_ceiling": "textarea",
  "in_target_company_compensation_according_to_proportion_flag": "checkbox",
  "in_proportion_to_shareholding_in_listed_companies_flag": "checkbox",
  "compensation_compensation_in_other_proportions": "textarea",
  "joint_several_compensation_flag": "checkbox",
  "supplementary_compensation_flag": "checkbox",
  "calculating_amount_of_compensable_cash_method": "textarea",
  "compensable_cash_amount_adjustment": "textarea",
  "other_assets_recognized_by_listed_companies_compensation": "textarea"
}

# 业绩预测补偿-补偿实施-table
performance_forecast_compensation_compensation_implementation_key_value_list = {
  "commitment_to_net_profit_flag": "承诺净利润",
  "commitment_to_net_operating_cash_flow_flag": "承诺经营性现金流量净额",
  "commitment_to_sign_contract_amount_flag": "承诺签订合同金额",
  "commitment_to_accounts_receivable_flag": "承诺应收账款",
  "committed_inventory_flag": "承诺存货",
  "commitment_to_long_term_receivables_flag": "承诺长期应收款",
}

performance_forecast_compensation_compensation_implementation_key_type_list = {
  "commitment_to_net_profit_flag": "checkbox",
  "commitment_to_net_operating_cash_flow_flag": "checkbox",
  "commitment_to_sign_contract_amount_flag": "checkbox",
  "commitment_to_accounts_receivable_flag": "checkbox",
  "committed_inventory_flag": "checkbox",
  "commitment_to_long_term_receivables_flag": "checkbox"
}

# 业绩预测补偿-补偿实施-承诺净利润经营性现金流量金额/签订合同金额-股份补偿-table
to_net_profit_contract_amount_amount_share_compensation_key_value_list = {
  "share_repurchase_cancellation_flag": "股份回购注销",
  "charge_share_transfer_free_flag": "股份无偿划转",
  "share_presentation_flag": "股份赠送",
}

to_net_profit_contract_amount_amount_share_compensation_key_type_list = {
  "share_repurchase_cancellation_flag": "checkbox",
  "charge_share_transfer_free_flag": "checkbox",
  "share_presentation_flag": "checkbox"
}

# 业绩预测补偿-补偿实施-承诺净利润经营性现金流量金额/签订合同金额-现金补偿-table
to_net_profit_contract_amount_amount_cash_compensation_key_value_list = {
  "direct_cash_payment_flag": "直接现金支付",
  "cash_compensation_special_account_flag": "现金补偿专用账户",
}

to_net_profit_contract_amount_amount_cash_compensation_key_type_list = {
  "direct_cash_payment_flag": "checkbox",
  "cash_compensation_special_account_flag": "checkbox"
}

# 业绩预测补偿-补偿实施-承诺存货-现金补偿-table
implementation_committed_inventory_cash_compensation_key_value_list = {
  "direct_cash_payment_flag": "直接现金支付",
  "cash_compensation_special_account_flag": "现金补偿专用账户",
  "bond_flag": "保证金",
  "other_assets_payment": "其他资产支付",
}

implementation_committed_inventory_cash_compensation_key_type_list = {
  "direct_cash_payment_flag": "checkbox",
  "cash_compensation_special_account_flag": "checkbox",
  "bond_flag": "checkbox",
  "other_assets_payment": "textarea"
}

# 业绩预测补偿-补偿实施-应收账款-现金补偿-table
implementation_accounts_receivable_cash_compensation_key_value_list = {
  "direct_cash_payment_flag": "直接现金支付",
  "cash_compensation_special_account_flag": "现金补偿专用账户",
  "bond_flag": "保证金",
  "other_assets_payment": "其他资产支付",
}

implementation_accounts_receivable_cash_compensation_key_type_list = {
  "direct_cash_payment_flag": "checkbox",
  "cash_compensation_special_account_flag": "checkbox",
  "bond_flag": "checkbox",
  "other_assets_payment": "textarea"
}

# 业绩预测补偿-补偿实施-长期应收款-现金补偿-table
implementation_long_term_receivables_cash_compensation_key_value_list = {
  "direct_cash_payment_flag": "直接现金支付",
  "cash_compensation_special_account_flag": "现金补偿专用账户",
  "bond_flag": "保证金",
  "other_assets_payment": "其他资产支付",
}

implementation_long_term_receivables_cash_compensation_key_type_list = {
  "direct_cash_payment_flag": "checkbox",
  "cash_compensation_special_account_flag": "checkbox",
  "bond_flag": "checkbox",
  "other_assets_payment": "textarea"
}

# 业绩预测补偿担保-form
performance_forecast_compensation_guarantee_key_value_list = {
  "guarantee": "担保人",
  "identity": "身份",
  "guarantee_mode_share_pledge_guarantee_flag": "担保方式-股份质押担保",
  "guarantee_mode_margin_guarantee_flag": "担保方式-保证金担保",
}

performance_forecast_compensation_guarantee_key_type_list = {
  "guarantee": "text",
  "identity": "text",
  "guarantee_mode_share_pledge_guarantee_flag": "checkbox",
  "guarantee_mode_margin_guarantee_flag": "checkbox"
}

# 业绩预测担保-担保方式-股份质押担保-form
forecast_guarantee_guarantee_mode_share_pledge_guarantee_key_value_list = {
  "pledgor": "质押人",
  "pledge_subject": "质押担保对象",
  "pledge_subject_matter": "质押标的",
  "pledge_subject_computation_method": "质押标的计算方式",
  "pledgee": "质押权人",
  "pledge_period": "质押期间",
  "profits_during_pledge_period_distribution": "质押期间利润分配",
  "pledge_lifting_relieving_conditions": "解除质押-解除条件",
  "pledge_lifting_relief_ratio": "解除质押-解除比例",
  "pledge_lifting_relieving_formalities": "解除质押-解除手续",
  "pledge_lifting_removable_share_quantity_adjustment": "解除质押-可解除股份数量调整",
  "can_be_pledged_again_flag": "是否可以再次质押",
}

forecast_guarantee_guarantee_mode_share_pledge_guarantee_key_type_list = {
  "pledgor": "text",
  "pledge_subject": "text",
  "pledge_subject_matter": "textarea",
  "pledge_subject_computation_method": "textarea",
  "pledgee": "text",
  "pledge_period": "text",
  "profits_during_pledge_period_distribution": "textarea",
  "pledge_lifting_relieving_conditions": "textarea",
  "pledge_lifting_relief_ratio": "textarea",
  "pledge_lifting_relieving_formalities": "textarea",
  "pledge_lifting_removable_share_quantity_adjustment": "textarea",
  "can_be_pledged_again_flag": "checkbox"
}

# 业绩预测担保-担保方式-保证金担保-form
performance_forecast_guarantee_guarantee_mode_margin_guarantee_key_value_list = {
  "guarantor": "保证人",
  "margin_guarantee_object": "保证金担保对象",
  "margin_payment_method_cash": "保证金缴纳方式-现金",
  "margin_payment_method_share_pledge": "保证金缴纳方式-股份质押",
  "margin_calculation_method_cash": "保证金计算方式-现金",
  "margin_calculation_method_share_pledge": "保证金计算方式-股份质押",
  "margin_account_management": "保证金账户管理",
  "guaranty_period": "保证期间",
  "profit_distribution_during_guarantee_period": "保证期间利润分配",
  "margin_return_restitution_conditions": "保证金返还-返还条件",
  "margin_return_restitution_amount": "保证金返还-返还数额",
  "margin_return_restitution_procedures": "保证金返还-返还手续",
  "margin_return_return_amount_adjustment": "保证金返还-返还数额调整",
}

performance_forecast_guarantee_guarantee_mode_margin_guarantee_key_type_list = {
  "guarantor": "text",
  "margin_guarantee_object": "text",
  "margin_payment_method_cash": "textarea",
  "margin_payment_method_share_pledge": "textarea",
  "margin_calculation_method_cash": "textarea",
  "margin_calculation_method_share_pledge": "textarea",
  "margin_account_management": "text",
  "guaranty_period": "text",
  "profit_distribution_during_guarantee_period": "textarea",
  "margin_return_restitution_conditions": "textarea",
  "margin_return_restitution_amount": "textarea",
  "margin_return_restitution_procedures": "textarea",
  "margin_return_return_amount_adjustment": "textarea"
}

# 业绩承诺完成情况-form
performance_commitment_completion_key_value_list = {
  "committed_person": "承诺人",
  "identity": "身份",
  "stock_ratio": "股权比例（%）",
  "year": "年度",
  "actual_performance_amount": "实际业绩数额(万元）",
  "performance_commitment_amount": "业绩承诺数额（万元）",
  "difference": "差额（万元）",
  "completion_rate": "完成率（%）",
}

performance_commitment_completion_key_type_list = {
  "committed_person": "text",
  "identity": "text",
  "stock_ratio": "ratio",
  "year": "text",
  "actual_performance_amount": "decimal",
  "performance_commitment_amount": "decimal",
  "difference": "decimal",
  "completion_rate": "ratio"
}

# 减值测试时间-table
impairment_test_time_key_value_list = {
  "profit_commitment_period_expiration": "盈利承诺期届满",
  "each_fiscal_year_end": "每个会计年度结束",
}

impairment_test_time_key_type_list = {
  "profit_commitment_period_expiration": "text",
  "each_fiscal_year_end": "text"
}

# 减值测试流程-table
impairment_test_flow_key_value_list = {
  "how_to_determine_accounting_firms": "会计师事务所确定方式",
}

impairment_test_flow_key_type_list = {
  "how_to_determine_accounting_firms": "text"
}

# 减值测试补偿条件-table
impairment_test_compensation_conditions_key_value_list = {
  "during_profit_commitment_period_final_impairment_flag": "标的资产期末减值额大于利润承诺期累计已补偿总金额（已补偿股份数*每股发行价格+已补偿现金）",
  "items_to_be_deducted_from_impairment": "减值额需扣除项目",
}

impairment_test_compensation_conditions_key_type_list = {
  "during_profit_commitment_period_final_impairment_flag": "checkbox",
  "items_to_be_deducted_from_impairment": "textarea"
}

# 减值测试补偿安排-补偿金额-form
testing_compensation_arrangement_compensation_amount_key_value_list = {
  "compensatory_obligor": "补偿义务人",
  "compensatory_obligor_status": "补偿义务人身份",
  "compensation_amount_calculation_formula": "补偿金额计算公式",
  "compensation_amount_upper_limit": "补偿金额上限",
}

testing_compensation_arrangement_compensation_amount_key_type_list = {
  "compensatory_obligor": "text",
  "compensatory_obligor_status": "text",
  "compensation_amount_calculation_formula": "textarea",
  "compensation_amount_upper_limit": "textarea"
}

# 减值测试补偿安排-补偿方式-form
impairment_testing_compensation_arrangement_compensation_mode_key_value_list = {
  "compensatory_obligor": "补偿义务人",
  "compensatory_obligor_status": "补偿义务人身份",
  "share_compensation_flag": "股份补偿",
  "cash_compensation_flag": "现金补偿",
  "share_compensation_priority_flag": "股份补偿优先",
  "share_compensation_trigger_condition": "股份补偿触发条件",
  "cash_compensation_priority_flag": "现金补偿优先",
  "cash_compensation_trigger_conditions": "现金补偿触发条件",
  "compensation_compensation_in_proportion_to_shareholding": "补偿义务分配-按持股比例补偿",
  "compensation_compensation_in_other_proportions": "补偿义务分配-按其他比例补偿",
  "compensation_share_number_calculating_method": "补偿股份数计算方式",
  "calculating_amount_of_compensatory_cash_method": "补偿现金数量计算方式",
  "cash_compensation_proportional_commitment_flag": "现金补偿义务分配-比例承担",
  "compensation_each_party_undertakes_how_to_calculate_amount": "交易对方各自承担的补偿金额的计算方式",
  "cash_dividend_compensation_flag": "现金股利一并补偿",
  "cash_dividend_calculation_period": "现金股利计算期间",
  "compensation_obligation_joint_several_liability_flag": "是否对补偿义务连带责任",
  "compensation_implementation_time": "补偿实施时间",
}

impairment_testing_compensation_arrangement_compensation_mode_key_type_list = {
  "compensatory_obligor": "text",
  "compensatory_obligor_status": "text",
  "share_compensation_flag": "checkbox",
  "cash_compensation_flag": "checkbox",
  "share_compensation_priority_flag": "checkbox",
  "share_compensation_trigger_condition": "textarea",
  "cash_compensation_priority_flag": "checkbox",
  "cash_compensation_trigger_conditions": "textarea",
  "compensation_compensation_in_proportion_to_shareholding": "textarea",
  "compensation_compensation_in_other_proportions": "textarea",
  "compensation_share_number_calculating_method": "textarea",
  "calculating_amount_of_compensatory_cash_method": "textarea",
  "cash_compensation_proportional_commitment_flag": "checkbox",
  "compensation_each_party_undertakes_how_to_calculate_amount": "textarea",
  "cash_dividend_compensation_flag": "checkbox",
  "cash_dividend_calculation_period": "textarea",
  "compensation_obligation_joint_several_liability_flag": "checkbox",
  "compensation_implementation_time": "textarea"
}

# 减值测试补偿安排-补偿方式-减值补偿股份数量调整-form
mode_impairment_compensation_share_quantity_adjustment_key_value_list = {
  "adjustment_situation": "调整情形",
  "adjust_calculation_formula": "调整计算公式",
}

mode_impairment_compensation_share_quantity_adjustment_key_type_list = {
  "adjustment_situation": "text",
  "adjust_calculation_formula": "textarea"
}

# 减值测试补偿安排-补偿方式-股份补偿实施-form
compensation_mode_share_compensation_implementation_key_value_list = {
  "compensatory_obligor": "补偿义务人",
  "compensatory_obligor_status": "补偿义务人身份",
  "share_compensation_operation_arrangement": "股份补偿操作安排",
  "companies_share_repurchase_write_off_scheme_review_process": "股份回购注销方案上市公司审议流程",
  "compensation_obligator_share_transfer": "补偿义务人股份过户",
  "share_cancellation": "股份注销办理",
}

compensation_mode_share_compensation_implementation_key_type_list = {
  "compensatory_obligor": "text",
  "compensatory_obligor_status": "text",
  "share_compensation_operation_arrangement": "textarea",
  "companies_share_repurchase_write_off_scheme_review_process": "textarea",
  "compensation_obligator_share_transfer": "textarea",
  "share_cancellation": "textarea"
}

# 减值测试补偿安排-补偿方式-现金补偿实施-form
arrangement_compensation_mode_cash_compensation_implementation_key_value_list = {
  "compensatory_obligor": "补偿义务人",
  "compensatory_obligor_status": "补偿义务人身份",
  "direct_cash_compensation_flag": "是否直接现金补偿",
  "cash_compensation_opening_special_account_flag": "是否开立现金补偿专用账户",
  "agreements_with_listed_companies_commercial_banks_flag": "是否与上市公司、商业银行签订三方监管协议",
  "companies_to_determine_amount_impairment_compensation_time": "上市公司确定减值补偿金额时间",
  "process_determining_amount_of_impairment_compensation": "上市公司确定减值补偿金额流程",
  "performance_compensation_obligation_time_limit": "补偿义务履行期限",
  "performing_compensation_obligation_way": "补偿义务履行方式",
}

arrangement_compensation_mode_cash_compensation_implementation_key_type_list = {
  "compensatory_obligor": "text",
  "compensatory_obligor_status": "text",
  "direct_cash_compensation_flag": "checkbox",
  "cash_compensation_opening_special_account_flag": "checkbox",
  "agreements_with_listed_companies_commercial_banks_flag": "checkbox",
  "companies_to_determine_amount_impairment_compensation_time": "text",
  "process_determining_amount_of_impairment_compensation": "textarea",
  "performance_compensation_obligation_time_limit": "textarea",
  "performing_compensation_obligation_way": "textarea"
}

# 减值测试补偿安排-补偿方式-现金补偿实施-现金补偿专用账户-form
compensation_implementation_cash_compensation_special_account_key_value_list = {
  "compensatory_obligor": "补偿义务人",
  "compensatory_obligor_status": "补偿义务人身份",
  "attention_of_listed_companies_duty": "上市公司注意义务",
  "funs_restrictions_on_use": "账户内资金使用限制",
  "funs_rights_restriction": "账户内资金权利限制",
  "funs_transition_condition": "账户内资金转出条件",
  "funs_roll_out_restriction": "账户内资金转出限制",
}

compensation_implementation_cash_compensation_special_account_key_type_list = {
  "compensatory_obligor": "text",
  "compensatory_obligor_status": "text",
  "attention_of_listed_companies_duty": "textarea",
  "funs_restrictions_on_use": "textarea",
  "funs_rights_restriction": "textarea",
  "funs_transition_condition": "textarea",
  "funs_roll_out_restriction": "textarea"
}

# 减值测试补偿安排-补偿方式-现金补偿实施-现金补偿专用账户-专用账户内资金转出比例限制-table
special_account_special_funs_outbound_proportional_limitation_key_value_list = {
  "first_year": "第一年",
  "first_year_transfer_ratio_limit": "第一年转出比例限制(%)",
  "second_years": "第二年",
  "transfer_proportion_limitation_in_second_year": "第二年转出比例限制(%)",
  "third_year": "第三年",
  "third_year_transfer_ratio_limit": "第三年转出比例限制(%)",
}

special_account_special_funs_outbound_proportional_limitation_key_type_list = {
  "first_year": "text",
  "first_year_transfer_ratio_limit": "ratio",
  "second_years": "text",
  "transfer_proportion_limitation_in_second_year": "ratio",
  "third_year": "text",
  "third_year_transfer_ratio_limit": "ratio"
}

# 奖励期间-table
reward_period_key_value_list = {
  "earnings_commitment_period_flag": "盈利承诺期",
  "first_year": "第一年",
  "second_years": "第二年",
  "third_year": "第三年",
  "fourth_years": "第四年",
  "fifth_years": "第五年",
}

reward_period_key_type_list = {
  "earnings_commitment_period_flag": "checkbox",
  "first_year": "text",
  "second_years": "text",
  "third_year": "text",
  "fourth_years": "text",
  "fifth_years": "text"
}

# 触发条件-table
trigger_condition_key_value_list = {
  "performance_commitment_completed_in_each_year_flag": "各年度是否均完成业绩承诺",
  "accumulated_net_profit_excess_flag": "累计净利润是否超额",
  "accumulated_net_profit_excess_ratio": "累计净利润超额比例（%）",
  "operating_cash_flow_net_excess_flag": "经营性现金流量净额是否超额",
  "operating_cash_flow_net_excess_ratio": "经营性现金流量净额超额比例(%)",
  "contract_signed_excess_amount_flag": "签订合同金额是否超额",
  "contract_amount_excess_proportion": "签订合同金额超额比例(%)",
}

trigger_condition_key_type_list = {
  "performance_commitment_completed_in_each_year_flag": "checkbox",
  "accumulated_net_profit_excess_flag": "checkbox",
  "accumulated_net_profit_excess_ratio": "ratio",
  "operating_cash_flow_net_excess_flag": "checkbox",
  "operating_cash_flow_net_excess_ratio": "ratio",
  "contract_signed_excess_amount_flag": "checkbox",
  "contract_amount_excess_proportion": "ratio"
}

# 考核指标-form
assessment_index_key_value_list = {
  "assessment_indicators_types": "考核指标类型",
  "evaluation_indicator_calculation_formula": "考核指标计算公式",
  "deduction_items_type": "扣除项目类型",
}

assessment_index_key_type_list = {
  "assessment_indicators_types": "text",
  "evaluation_indicator_calculation_formula": "textarea",
  "deduction_items_type": "text"
}

# 奖励金额-form
reward_amount_key_value_list = {
  "amount_upper_limit": "数额上限",
  "cumulative_calculation_flag": "累计计算",
  "cumulative_calculation_formula": "累计计算公式",
  "stage_calculation_flag": "分期计算",
  "phase_i_calculation_formula": "第一期计算公式",
  "phase_ii_calculation_formula": "第二期计算公式",
  "phase_iii_calculation_formula": "第三期计算公式",
  "not_calculated_according_to_excess_range_flag": "不按超额幅度计算",
  "do_not_calculate_formula_according_to_excess_range_flag": "不按超额幅度计算公式",
  "calculated_by_excess_range_in_segments_flag": "按超额幅度分段式计算",
  "paragraph_one_excess_range": "第一段超额幅度",
  "paragraph_one_incentive_amount": "第一段奖励金额",
  "paragraph_two_excess_range": "第二段超额幅度",
  "paragraph_two_incentive_amount": "第二段奖励金额",
}

reward_amount_key_type_list = {
  "amount_upper_limit": "textarea",
  "cumulative_calculation_flag": "checkbox",
  "cumulative_calculation_formula": "textarea",
  "stage_calculation_flag": "checkbox",
  "phase_i_calculation_formula": "textarea",
  "phase_ii_calculation_formula": "textarea",
  "phase_iii_calculation_formula": "textarea",
  "not_calculated_according_to_excess_range_flag": "checkbox",
  "do_not_calculate_formula_according_to_excess_range_flag": "checkbox",
  "calculated_by_excess_range_in_segments_flag": "checkbox",
  "paragraph_one_excess_range": "textarea",
  "paragraph_one_incentive_amount": "textarea",
  "paragraph_two_excess_range": "textarea",
  "paragraph_two_incentive_amount": "textarea"
}

# 支付安排-form
payment_arrangements_key_value_list = {
  "payment_body": "支付主体",
  "reward_object_name": "奖励对象名称",
  "reward_object_identity": "奖励对象身份",
  "one_time_payment_flag": "一次性支付",
  "installment_payment_flag": "分期支付",
  "installment_payment_arrangement": "分期支付安排",
  "cash_payment_flag": "现金支付",
  "other_payments": "其他支付方式",
  "payment_time": "支付时间",
}

payment_arrangements_key_type_list = {
  "payment_body": "text",
  "reward_object_name": "text",
  "reward_object_identity": "text",
  "one_time_payment_flag": "checkbox",
  "installment_payment_flag": "checkbox",
  "installment_payment_arrangement": "textarea",
  "cash_payment_flag": "checkbox",
  "other_payments": "textarea",
  "payment_time": "textarea"
}

# 账务处理-table
accounting_treatment_key_value_list = {
  "reward_not_deducted_from_net_profit_realized_amount_flag": "奖励金额不从净利润实现额中扣除",
  "net_profit_not_affected_actual_accounting_treatment_flag": "净利润的实际会计处理不受影响",
  "incentive_amount_deducted_from_personal_income_tax_flag": "奖励金额是否扣除个人所得税",
}

accounting_treatment_key_type_list = {
  "reward_not_deducted_from_net_profit_realized_amount_flag": "checkbox",
  "net_profit_not_affected_actual_accounting_treatment_flag": "checkbox",
  "incentive_amount_deducted_from_personal_income_tax_flag": "checkbox"
}
