

def get_drift_report(base_df,current_df,threshold=0.5):
    report={}
    for column in base_df.columns:
        d1=base_df[column]
        d2=current_df[column]
        is_same_dist=ks_2samp(d1,d2)
        if is_same_dist.pvalue >= threshold:
            is_found=False
        else:
            is_found=True
            report.update({column:{"p_value":is_same_dist.pvalue,
                                   "drift_status":is_found}})
        
    return report