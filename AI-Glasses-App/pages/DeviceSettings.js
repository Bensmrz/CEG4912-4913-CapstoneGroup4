import { StatusBar } from 'expo-status-bar'
import React, { useState } from 'react';
import { StyleSheet, View, TextInput, Text, Button} from 'react-native';
import Navbar from "./../assets/components/Navbar";
import { ListItem, ButtonGroup, Header } from '@rneui/themed';
import Overlay from "./../assets/components/Overlay";

function DeviceSettings(){
  return(
    <>
      <Header
      backgroundImageStyle={{}}
      barStyle="default"
      centerComponent={{
        text: "Device Settings",
        style: { color: "#fff" }
      }}
      centerContainerStyle={{}}
      containerStyle={{ width: 450 }}
      leftComponent={{ icon: "menu", color: "#fff" }}
      leftContainerStyle={{}}
      linearGradientProps={{}}
      placement="center"
      rightComponent={{ icon: "home", color: "#fff" }}
      rightContainerStyle={{}}
      statusBarProps={{}}
      />
      <Overlay />
      <Button
        title="Enable Conversation Log"
        onPress={() => console.log("Enable Conversation log Pressed!")}
      />
      <Button
        title="Language Conversion:"
        onPress={() => console.log("Language Conversion Pressed!")}
      />
    </> 
  )
}
const styles = StyleSheet.create({
  button: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
export default DeviceSettings