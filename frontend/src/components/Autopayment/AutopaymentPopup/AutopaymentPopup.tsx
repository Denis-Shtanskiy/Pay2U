import { Box, Modal, Typography } from '@mui/material';
import FilterPopupBtn from '../../../assets/FilterPopupBtn.svg?react';
import AutopayConnectIcon from '../../../assets/AutopayConnectIcon.svg?react';
import SubmitButton from '../../SubmitBtn/SubmitBtn';
import { useNavigate } from 'react-router-dom';
import { AutopaymentPopupData } from '../../../utils/constants';

interface FiltersPopupSelectProps {
  open: boolean;
  onClose: () => void;
}

export default function AutopaymentPopup({ open, onClose }: FiltersPopupSelectProps) {
  const navigate = useNavigate();
  const styles = {
    container: { backgroundColor: 'rgba(0, 0, 0, 0.5)' },
    title: {
      fontFamily: 'Inter',
      fontSize: '18px',
      fontWeight: '700'
    },
    done: { display: 'flex', flexDirection: 'column', alignItems: 'center' },
    sum: { fontFamily: 'Inter', fontSize: '16px', fontWeight: '700' },
    subtitle: { fontFamily: 'Inter', fontSize: '14px', fontWeight: '400', paddingTop: '5px' },
    date: { color: '#E86513' },
    popover: {
      padding: '12px 20px 64px',
      backgroundColor: '#fff',
      borderRadius: '16px',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      position: 'fixed',
      top: '400px',
      left: 0,
      width: '335px'
    },
    icon: { width: '74px', height: '74px', margin: '20px 0' },
    text: { margin: '30px 0 ', textAlign: 'center' }
  };

  const handleApplyClick = () => {
    onClose();
    navigate('/services');
    window.scroll(0, 0);
  };

  return (
    <Modal sx={styles.container} open={open} onClose={onClose}>
      <Box sx={styles.popover}>
        <Box sx={styles.done}>
          <FilterPopupBtn />
          <AutopayConnectIcon style={styles.icon} />
          <Typography sx={styles.title}>{AutopaymentPopupData.title}</Typography>
        </Box>
        <Box sx={styles.text}>
          <Typography sx={styles.sum}>199 &#8381;</Typography>
          <Typography sx={styles.subtitle}>
            {AutopaymentPopupData.nextPay}{' '}
            <span style={styles.date}>{AutopaymentPopupData.date}.</span>
          </Typography>
          <Typography sx={styles.subtitle}>{AutopaymentPopupData.text}</Typography>
        </Box>
        <SubmitButton
          title="Вернуться на главную"
          width="335px"
          height="56px"
          onClick={handleApplyClick}
        />
      </Box>
    </Modal>
  );
}
