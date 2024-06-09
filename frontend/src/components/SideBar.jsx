import React from 'react';
import { Box, Flex, Avatar, VStack, IconButton, Divider } from '@chakra-ui/react';
import { FaHome, FaBell, FaCog, FaVideo } from 'react-icons/fa';

const Sidebar = () => {
  return (
    <Box bg="blue.400" color="white"
      borderRadius={8}
      p={4}
      h="90vh"
    >
      <Flex py={2} justifyContent={"center"}>
        <Avatar bg="tan" size="md" name="User Name" />
      </Flex>

      <Divider my={4} />
      
      <VStack spacing={4} align="stretch">
        <IconButton
          icon={<FaHome />}
          aria-label="Home"
          colorScheme="white"
          variant="ghost"
          fontSize="20px"
          _hover={{ bg: 'blue.500' }}
        />
        <IconButton
          icon={<FaBell />}
          aria-label="Notifications"
          colorScheme="white"
          variant="ghost"
          fontSize="20px"
          _hover={{ bg: 'blue.500' }}
        />
        <IconButton
          icon={<FaCog />}
          aria-label="Settings"
          colorScheme="white"
          variant="ghost"
          fontSize="20px"
          _hover={{ bg: 'blue.500' }}
        />
        <IconButton
          icon={<FaVideo />}
          aria-label="Video"
          colorScheme="white"
          variant="ghost"
          fontSize="20px"
          _hover={{ bg: 'blue.500' }}
        />
      </VStack>

    </Box>
  );
};

export default Sidebar;
