from pyspark.sql import HiveContext
hive_context = HiveContext(sc)
df2=hive_context.table("bigfoot_external_neo.cp_affordability__fintech_loan_subapplication_fact")
df2=df2.drop("data","id","application_id","created_at_time_key","autopay_mandatory","autopay_applicable","autopay_failed_retry_count","check_eligibility_credit_amount","eligible_for_credit","autopay_failure_reason","fldg_applicable")
df3=hive_context.table("bigfoot_external_neo.cp_cremo__cremo_bnpl_payback_fact")
df3=df3.drop("product","statement_id","year","month","revolve_flag","due_date","non_rev_due_date","last_payback_date","gross_amount","net_amount","overdue_amount","txn_rank","old_account_id")
df=df2.join(df3,None,"outer")