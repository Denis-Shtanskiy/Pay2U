import { Box, Typography } from '@mui/material';
import ServicesInstruction from '../../../Instructions/ServiseInstructions/ServicesInstruction';
import PartnerSite from '../../../Instructions/PartnerSite/PartnerSite';
import { ManageSubscriptionAboutPartnerData } from '../../../../utils/constants';

const styles = {
  container: { marginTop: '10px' },
  text: {
    marginTop: '20px',
    fontSize: '14px',
    fontWeight: '400',
    color: '#676879',
    fontFamily: 'Inter',
    lineHeight: '1.25',
    textAlign: 'start'
  }
};

export default function ManageSubscriptionAboutPartner() {
  return (
    <Box sx={styles.container}>
      <Typography sx={styles.text}>{ManageSubscriptionAboutPartnerData.text}</Typography>
      <PartnerSite />
      <ServicesInstruction marginTop="32px" />
    </Box>
  );
}