import { StatusBar } from 'expo-status-bar'
import { Button, Overlay, Icon } from '@rneui/themed';
import React, { useState } from 'react';
import { StyleSheet, View, TextInput, Text } from 'react-native';


type OverlayComponentProps = {};

const OverlayComponent: React.FunctionComponent<OverlayComponentProps> = () => {
const [visible, setVisible] = useState(false);

const toggleOverlay = () => {
  setVisible(!visible);
};

return (
  <View>
    <Button
      title="Manage Connections"
      onPress={toggleOverlay}
      buttonStyle={styles.button}
    />
    <Overlay isVisible={visible} onBackdropPress={toggleOverlay}>
      <Text style={styles.textPrimary}>Connections</Text>
      <Text style={styles.textSecondary}>
        Choose a Connection to Edit
      </Text>
      <Button
        icon={
          <Icon
            name="wrench"
            type="font-awesome"
            color="white"
            size={25}
            iconStyle={{ marginRight: 10 }}
          />
        }
        title="iPhone"
        onPress={toggleOverlay}
      />
      <Button
        icon={
          <Icon
            name="wrench"
            type="font-awesome"
            color="white"
            size={25}
            iconStyle={{ marginVertical: 10 }}
          />
        }
        title="Speakers"
        onPress={toggleOverlay}
      />
      <Button
        icon={
          <Icon
            name="wrench"
            type="font-awesome"
            color="white"
            size={25}
            iconStyle={{ marginRight: 10 }}
          />
        }
        title="Microphone"
        onPress={toggleOverlay}
      />
    </Overlay>
  </View>
);
};

const styles = StyleSheet.create({
button:{
  margin: 50,
},
textPrimary: {
  marginVertical: 20,
  textAlign: 'center',
  fontSize: 20,
},
textSecondary: {
  marginBottom: 10,
  textAlign: 'center',
  fontSize: 17,
},
});


export default OverlayComponent;